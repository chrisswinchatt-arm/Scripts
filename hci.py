#!/usr/bin/env python3

#05:00:d9:1a:05:00:fd:02:05:00:dd:1a:05:00:09:03:05:00:0f:03:05:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:bd:01:00

from enum import Enum
import sys

class HciMessageType(Enum):
    CMD = 1
    ACL = 2
    SYNC = 3
    EVT = 4
    ISO = 5

class HciCommand(Enum):
    Inquiry = (1, 0x1)
    Inquiry_Cancel = (1, 0x2)
    Periodic_Inquiry_Mode = (1, 0x3)
    Exit_Periodic_Inquiry_Mode = (1, 0x4)
    Create_Connection = (1, 0x5)
    Disconnect = (1, 0x6)
    Add_SCO_Connection = (1, 0x7)
    Accept_Connection_Request = (1, 0x9)
    Reject_Connection_Request = (1, 0xA)
    Link_Key_Request_Reply = (1, 0xB)
    Link_Key_Request_Negative_Reply = (1, 0xC)
    PIN_Code_Request_Reply = (1, 0xD)
    PIN_Code_Request_Negative_Reply = (1, 0xE)
    Change_Connection_Packet_Type = (1, 0xF)
    Authentication_Requested = (1, 0x11)
    Set_Connection_Encryption = (1, 0x13)
    Change_Connection_Link_Key = (1, 0x15)
    Master_Link_Key = (1, 0x17)
    Remote_Name_Request = (1, 0x19)
    Read_Remote_Supported_Features = (1, 0x1B)
    Read_Remote_Version_Information = (1, 0x1D)
    Read_Clock_Offset = (1, 0x1F)

    Hold_Mode = (2, 0x1)
    Sniff_Mode = (2, 0x3)
    Exit_Sniff_Mode = (2, 0x4)
    Park_Mode = (2, 0x5)
    Exit_Park_Mode = (2, 0x6)
    QoS_Setup = (2, 0x7)
    Role_Discovery = (2, 0x9)
    Switch_Role = (2, 0xB)
    Read_Link_Policy_Settings = (2, 0xC)
    Write_Link_Policy_Settings = (2, 0xD)

    Set_Event_Mask = (3,0x1)
    Reset = (3,0x3)
    Set_Event_Filter = (3,0x5)
    Flush = (3,0x8)
    Read_PIN_Type = (3,0x9)
    Write_PIN_Type = (3,0xA)
    Create_New_Unit_Key = (3,0xB)
    Read_Stored_Link_Key = (3,0xD)
    Write_Stored_Link_Key = (3,0x11)
    Delete_Stored_Link_Key = (3,0x12)
    Change_Local_Name = (3,0x13)
    Read_Local_Name = (3,0x14)
    Read_Connection_Accept_Timeout = (3,0x15)
    Write_Connection_Accept_Timeout = (3,0x16)
    Read_Page_Timeout = (3,0x17)
    Write_Page_Timeout = (3,0x18)
    Read_Scan_Enable = (3,0x19)
    Write_Scan_Enable = (3,0x1A)
    Read_Page_Scan_Activity = (3,0x1B)
    Write_Page_Scan_Activity = (3,0x1C)
    Read_Inquiry_Scan_Activity = (3,0x1D)
    Write_Inquiry_Scan_Activity = (3,0x1E)
    Read_Authentication_Enable = (3,0x1F)
    Write_Authentication_Enable = (3,0x20)
    Read_Encryption_Mode = (3,0x21)
    Write_Encryption_Mode = (3,0x22)
    Read_Class_Of_Device = (3,0x23)
    Write_Class_Of_Device = (3,0x24)
    Read_Voice_Setting = (3,0x25)
    Write_Voice_Setting = (3,0x26)
    Read_Automatic_Flush_Timeout = (3,0x27)
    Write_Automatic_Flush_Timeout = (3,0x28)
    Read_Num_Broadcast_Retransmissions = (3,0x29)
    Write_Num_Broadcast_Retransmissions = (3,0x2A)
    Read_Hold_Mode_Activity = (3,0x2B)
    Write_Hold_Mode_Activity = (3,0x2C)
    Read_Transmit_Power_Level = (3,0x2D)
    Read_SCO_Flow_Control_Enable = (3,0x2E)
    Write_SCO_Flow_Control_Enable = (3,0x2F)
    Set_Host_Controller_To_Host_Flow_Control = (3,0x31)
    Host_Buffer_Size = (3,0x33)
    Host_Number_Of_Completed_Packets = (3,0x35)
    Read_Link_Supervision_Timeout = (3,0x36)
    Write_Link_Supervision_Timeout = (3,0x37)
    Read_Number_Of_Supported_IAC = (3,0x38)
    Read_Current_IAC_LAP = (3,0x39)
    Write_Current_IAC_LAP = (3,0x3A)
    Read_Page_Scan_Period_Mode = (3,0x3B)
    Write_Page_Scan_Period_Mode = (3,0x3C)
    Read_Page_Scan_Mode = (3,0x3D)
    Write_Page_Scan_Mode = (3,0x3E)

    LE_Set_Event_Mask = (8, 0x1)
    LE_Read_Buffer_Size = (8, 0x2)
    LE_Read_Local_Supported_Features = (8, 0x3)
    LE_Set_Random_Address = (8, 0x5)
    LE_Set_Advertising_Parameters = (8, 0x6)
    LE_Read_Advertising_Physical_Channel_Tx_Power = (8, 0x7)
    LE_Set_Advertising_Data = (8, 0x8)
    LE_Set_Scan_Response_Data = (8, 0x9)
    LE_Set_Advertising_Enable = (8, 0xa)
    LE_Set_Scan_Parameters = (8, 0xb)
    LE_Set_Scan_Enable = (8, 0xc)
    LE_Create_Connection = (8, 0xd)
    LE_Create_Connection_Cancel = (8, 0xe)
    LE_Read_White_List_Size = (8, 0xf)
    LE_Clear_White_List = (8, 0x10)
    LE_Add_Device_To_White_List = (8, 0x11)
    LE_Remove_Device_From_White_List = (8, 0x12)
    LE_Connection_Update = (8, 0x13)
    LE_Set_Host_Channel_Classification = (8, 0x14)
    LE_Read_Channel_Map = (8, 0x15)
    LE_Read_Remote_Features = (8, 0x16)
    LE_Encrypt = (8, 0x17)
    LE_Rand = (8, 0x18)
    LE_Enable_Encryption = (8, 0x19)
    LE_Long_Term_Key_Request_Reply = (8, 0x1a)
    LE_Long_Term_Key_Request_Negative_Reply = (8, 0x1b)
    LE_Read_Supported_States = (8, 0x1c)
    LE_Receiver_Test = (8, 0x1d)
    LE_Transmitter_Test = (8, 0x1e)
    LE_Test_End = (8, 0x1f)
    LE_Remote_Connection_Parameter_Request_Reply = (8, 0x20)
    LE_Remote_Connection_Parameter_Request_Negative_Reply = (8, 0x21)
    LE_Set_Data_Length = (8, 0x22)
    LE_Read_Suggested_Default_Data_Length = (8, 0x23)
    LE_Write_Suggested_Default_Data_Length = (8, 0x24)
    LE_Read_Local_P256_Public_Key = (8, 0x25)
    LE_Generate_DHKey = (8, 0x26)
    LE_Add_Device_To_Resolving_List = (8, 0x27)
    LE_Remove_Device_From_Resolving_List = (8, 0x28)
    LE_Clear_Resolving_List = (8, 0x29)
    LE_Read_Resolving_List_Size = (8, 0x2a)
    LE_Read_Peer_Resolvable_Address = (8, 0x2b)
    LE_Read_Local_Resolvable_Address = (8, 0x2c)
    LE_Set_Address_Resolution_Enable = (8, 0x2d)
    LE_Set_Resolvable_Private_Address_Timeout = (8, 0x2e)
    LE_Read_Maximum_Data_Length = (8, 0x2f)
    LE_Read_PHY = (8, 0x30)
    LE_Set_Default_PHY = (8, 0x31)
    LE_Set_PHY = (8, 0x32)
    LE_Set_Advertising_Set_Random_Address = (8, 0x35)
    LE_Set_Extended_Advertising_Parameters = (8, 0x36)
    LE_Set_Extended_Advertising_Data = (8, 0x37)
    LE_Set_Extended_Scan_Response_Data = (8, 0x38)
    LE_Set_Extended_Advertising_Enable = (8, 0x39)
    LE_Read_Maximum_Advertising_Data_Length = (8, 0x3a)
    LE_Read_Number_Of_Supported_Advertising_Sets = (8, 0x3b)
    LE_Remove_Advertising_Set = (8, 0x3c)
    LE_Clear_Advertising_Sets = (8, 0x3d)
    LE_Set_Periodic_Advertising_Parameters = (8, 0x3e)
    LE_Set_Periodic_Advertising_Data = (8, 0x3f)
    LE_Set_Periodic_Advertising_Enable = (8, 0x40)
    LE_Set_Extended_Scan_Parameters = (8, 0x41)
    LE_Set_Extended_Scan_Enable = (8, 0x42)
    LE_Extended_Create_Connection = (8, 0x43)
    LE_Periodic_Advertising_Create_Sync = (8, 0x44)
    LE_Periodic_Advertising_Create_Sync_Cancel = (8, 0x45)
    LE_Periodic_advertising_Terminate_Sync = (8, 0x46)
    LE_Add_Device_To_Periodic_Advertiser_List = (8, 0x47)
    LE_Remove_Device_from_Periodic_Advertiser_List = (8, 0x48)
    LE_Clear_Periodic_Advertiser_List = (8, 0x49)
    LE_Read_Periodic_Advertiser_List_Size = (8, 0x4a)
    LE_Read_Transmit_Power = (8, 0x4b)
    LE_Read_RF_Path_Compensation = (8, 0x4c)
    LE_Write_RF_Path_Compensation = (8, 0x4d)
    LE_Set_Privacy_Mode = (8, 0x4e)
    # TODO

    @classmethod
    def find(cls, ogf, ocf):
        for cmd in list(cls):
            if cmd.ogf == ogf and cmd.ocf == ocf:
                return cmd
        raise IndexError(f'[OGF:OCF] = [{ogf:02x}:{ocf:04x}] = {ogf:06b} {ocf:010b}')

    def __init__(self, ogf, ocf):
        self.ogf = ogf
        self.ocf = ocf

class HciEvent(Enum):
    Inquiry_Complete_Event = 0x1
    Inquiry_Result_Event = 0x2
    Connection_Complete_Event = 0x3
    Connection_Request_Event = 0x4
    Disconnection_Complete_Event = 0x5
    Authentication_Complete_Event = 0x6
    Remote_Name_Request_Complete_Event = 0x7
    Encryption_Change_Event = 0x8
    Change_Connection_Link_Key_Complete_Event = 0x9
    Master_Link_Key_Complete_Event = 0xA
    Read_Remote_Supported_Features_Complete_Event = 0xB
    Read_Remote_Version_Complete_Event = 0xC
    Q0S_Setup_Complete_Event = 0xD
    Command_Complete_Event = 0xE
    Command_Status_Event = 0xF
    Hardware_Error_Event = 0x10
    Flush_Occured_event = 0x11
    Role_Change_Event = 0x12
    Number_Of_Completed_Packets_Event = 0x13
    Mode_Change_Event = 0x14
    Return_Link_Keys_Event = 0x15
    PIN_Code_Request_Event = 0x16
    Link_Key_Request_Event = 0x17
    Link_Key_Notification_Event = 0x18
    Loopback_Command_Event = 0x19
    Data_Buffer_Overflow_Event = 0x1A
    Max_Slots_Change_Event = 0x1B
    Read_Clock_Offset_Complete_Event = 0x1C
    Connection_Packet_Type_Changed_Event = 0x1D
    QoS_Violation_Event = 0x1E
    Page_Scan_Mode_Change_Event = 0x1F
    Page_Scan_Repetition_Mode_Change_Event = 0x20

class HciEventStatus(Enum):
    OK = 0

def dump_hci_command(bs):
    ogf = bs[1] >> 2          # OGF is the high 6 bits
    ocf = (bs[1] & 3) + bs[0] # OCF is the remaining 10 bits
    cmd = None
    try:
        cmd = HciCommand.find(ogf, ocf).name
    except IndexError:
        cmd = 'Unknown({:x}{:x})'.format(bs[0], bs[1])
    param_total_length = bs[2]
    l = len(bs)
    if param_total_length + 3 != l:
        print(f'Warn: command has param_total_length={param_total_length} but the packet has length {l}', file=sys.stderr)
    return '{} {}'.format(
        cmd,
        ':'.join(['{:02x}'.format(b) for b in bs[3:]])
    )

def dump_hci_event(bs):
    evt = None
    try:
        evt = HciEvent(bs[0]).name
    except ValueError:
        evt = 'Unknown({:02x})'.format(bs[0])
    status = None
    try:
        status = '{}({:02x})'.format(HciEventStatus(bs[1]).name, bs[1])
    except ValueError:
        evt = 'Unknown({:02x})'.format(bs[1])
    return '{} {} {}'.format(
        evt,
        status,
        ':'.join(['{:02x}'.format(b) for b in bs[2:]])
    )

def dump_hci_message(bs):
    type_ = HciMessageType(bs[0])
    if type_ == HciMessageType.CMD:
        s = dump_hci_command(bs[1:])
        if s:
            return 'HOST->LL CMD ' + s
        return None
    elif type_ == HciMessageType.EVT:
        s = dump_hci_event(bs[1:])
        if s:
            return 'LL->HOST EVT ' + s
        return None
    else:
        raise NotImplementedError(f'Unsupported message type: {bs[0]}')

def print_hci_message(bs, **kwargs):
    msg = dump_hci_message(bs)
    if msg:
        print(msg, **kwargs)

def show_usage(fp):
    print(
        (
            'Usage: {0}\n'+
            'Input: Encoded HCI packets (in xx:xx:xx format; one per line; lines starting with # are echoed)\n'+
            'Output: Decoded HCI packets\n'+
            'Example:\n'+
            '\t$ echo -e "#Command\\n01:03:0c:00" | {0}\n'+
            '\tCommand\n'+
            '\t[CMD] Reset\n\n'
            'Usage: {0} -mbed\n'
        ).format(sys.argv[0]),
        file=fp
    )

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] in ('-h','-help','--help'):
            show_usage(sys.stdout)
            exit(0)
        else:
            show_usage(sys.stderr)
            exit(1)

    end = '\n'
    for line in sys.stdin:
        if line.endswith('\n'):
            line = line[:-1]
        if line.endswith('\\'):
            line = line[:-1]
            end = ''

        if line.startswith('#'):
            print(line[1:], end=end)
        else:
            bs = []
            idx = 0
            for x in line.split(':'):
                if x.endswith('*'):
                    continue
                try:
                    x = int(x, base=16)
                    if x > 0xFF:
                        x = f'{x:02x}'
                        raise ValueError()
                except ValueError as e:
                    raise ValueError(f'Expected hex value of 00 to FF, got "{x}"')
                else:
                    bs.append(x)
            print_hci_message(bs, end=end)

        end = '\n'
