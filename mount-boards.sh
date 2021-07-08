export BOARDS_MOUNTS="/media/chrswi02"
export NRF52A="$BOARDS_MOUNTS/nrf52a"
export NRF52B="$BOARDS_MOUNTS/nrf52b"
export NRF52C="$BOARDS_MOUNTS/nrf52c"

function reload_mount_boards_sh {
    . "/home/chrswi02/Work/Scripts/mount-boards.sh"
}

function mount_boards {
    local type=$1
    local -A boards

    case "$type" in
        NRF52840_DK) ;;
        *)
            echo "$FUNCNAME: Unsupported device type \"$type\"" >&2
            return 1
        ;;
    esac

    echo "$FUNCNAME: Detecting boards of type \"$type\"..."
    while read line; do
        local board=$(echo "$line" | awk '{print $2}')
        local idx=$(echo "$line" | awk '{print $4}')
        local mp=$(echo "$line" | awk '{print $6}')
        local tty=$(echo "$line" | awk '{print $8}')
        local id=$(echo "$line" | awk '{print $10}')

        if [[ "$mp" != "unknown" ]]; then
            echo "$FUNCNAME: $idx: Already mounted" >&2
            continue
        fi

        # Extremely ugly: mount every /dev/sd* device on $tmp until we find the one that matches
        local found=0
        local tmp=$(mktemp -d)
        for dev in /dev/sd{b,c,d,e,f,g}; do
            mount "$dev" "$tmp" 2>/dev/null || continue
            local out=$(venv_mbedls 2>/dev/null | grep "$id")
            umount "$dev"

            if [[ "$out" != "" ]]; then
                found=1
                boards["$tty"]="$dev"
                break
            fi
        done 
        rm -rf "$tmp"

        if [[ $found -eq 0 ]]; then
            echo "$FUNCNAME: Could not mount $idx ($id)" >&2
            continue
        fi
    done < <(venv_mbedls -u | grep "$type")

    if [[ ${#boards[@]} -eq 0 ]]; then
        echo "$FUNCNAME: Could not mount any boards with type $type" >&2
        return 0
    fi

    # Mount the boards
    echo "$FUNCNAME: Mounting ${#boards[@]} detected boards"
    local suffixes=()
    case "$type" in
        NRF52840_DK)
            suffixes=(A B C)
            ;;
        *);;
    esac
    local suffix_idx=0
    local type_idx=0
    for tty in $(echo ${!boards[@]} | sort); do
        local prefix=
        case "$type" in
            NRF52840_DK) prefix=NRF52 ;;
            *);;
        esac

        local mp=$(eval echo \$${prefix}${suffixes[$suffix_idx]})
        mount "${boards[$tty]}" "$mp" || continue
        echo "$FUNCNAME: $type[$type_idx] (tty=$tty, dev=${boards[$tty]}) mounted on $mp"

        suffix_idx=$[suffix_idx + 1]
        type_idx=$[type_idx + 1]
    done
}

function mount_nrf52s {
    mount_boards "NRF52840_DK"
}

function umount_boards {
    count=0
    for mp in $BOARDS_MOUNTS/*; do
        umount "$mp" 2>/dev/null && count=$[count + 1]
    done
    echo "$FUNCNAME: $count boards unmounted"
}

function umount_nrf52s {
    umount "$NRF52A" "$NRF52B" "$NRF52C"
}

function board_cp {
    local file=$1
    shift

    while [[ $# -gt 0 ]]; do
        cp "$file" "$1"
        shift
    done

    sync
}

function nrf52_cp {
    board_cp "$1" "$NRF52A" "$NRF52B" "$NRF52C"
}

function board_errors {
    local num=$(find "$BOARDS_MOUNTS" -iname "fail.txt" | xargs wc -l)
    if [[ num -eq 0 ]]; then
        echo "$FUNCNAME: No failure reported" >&2
    else
        echo "$FUNCNAME: $num boards report errors:" >&2
        find "$BOARDS_MOUNTS" -iname "fail.txt" | xargs cat
    fi
}
