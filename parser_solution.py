import csv
from collections import defaultdict

def parse_lookup_table(lookup_file):
    lookup_dict = {}
    with open(lookup_file, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header
        for row in csv_reader:
            dstport, protocol, tag = row
            key = (dstport.lower(), protocol.lower())
            lookup_dict[key] = tag
    return lookup_dict

def parse_flow_logs(flow_file, lookup_dict):
    tag_counts = defaultdict(int)
    port_protocol_counts = defaultdict(int)
    
    with open(flow_file, mode='r') as file:
        for line in file:
            data = line.strip().split()
            if len(data) < 13:  # Ensure the line has enough elements
                continue
            dstport = data[6]
            protocol_num = data[7]
            
            # Convert protocol number to protocol name
            protocol = 'tcp' if protocol_num == '6' else 'udp' if protocol_num == '17' else 'icmp' if protocol_num == '1' else 'other'
            
            key = (dstport.lower(), protocol.lower())  # Ensure case insensitivity
            tag = lookup_dict.get(key, "Untagged")
            
            tag_counts[tag] += 1
            port_protocol_counts[key] += 1
    
    return tag_counts, port_protocol_counts

def write_output(tag_counts, port_protocol_counts, output_file):
    with open(output_file, mode='w') as file:
        file.write("Tag Counts:\n")
        file.write("Tag,Count\n")
        for tag, count in sorted(tag_counts.items()):
            file.write(f"{tag},{count}\n")
        
        file.write("\nPort/Protocol Combination Counts:\n")
        file.write("Port,Protocol,Count\n")
        for (port, protocol), count in sorted(port_protocol_counts.items()):
            file.write(f"{port},{protocol},{count}\n")

if __name__ == "__main__":
    lookup_file = "lookup_table.csv"
    flow_file = "flow_logs.txt"
    output_file = "output.txt"
    
    lookup_dict = parse_lookup_table(lookup_file)
    tag_counts, port_protocol_counts = parse_flow_logs(flow_file, lookup_dict)
    write_output(tag_counts, port_protocol_counts, output_file)
