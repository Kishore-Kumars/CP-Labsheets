#Problem Statment: Network Packet Integrity Check (Using XOR)
#Sample Input - Enter number of packets:  4
#Enter packet values:  10 20 30 40
#Enter checksum value:  15
#Sample Output - OK or ANOMALY

n = int(input("Enter number of packets: "))
packets = list(map(int, input("Enter packet values: ").strip().split()))

if len(packets) != n:
    print("ANOMALY")
else:
    checksum = int(input("Enter checksum value: "))
    xor_value = 0

    for packet in packets:
        xor_value ^= packet

    if xor_value == checksum:
        print("OK")
    else:
        print("ANOMALY")