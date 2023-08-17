import re
# import dummy
def cluster_cpu():
    raw = """Usage Summary In Cluster:*********************************************
CPU Utilization for 5 seconds = 0%; 1 minute: 1% 5 minutes: 0%


unit-1-1(kjkZfd):******************************************************
CPU Utilization for 5 seconds = 0%; 1 minute: 2% 5 minutes: 0%


unit-2-1:*************************************************************
CPU Utilization for 5 seconds = 0%; 1 minute: 6% 5 minutes: 0%

unit-3-1:*************************************************************
CPU Utilization for 5 seconds = 0%; 1 minute: 0% 5 minutes: 0%

unit-4-1:*************************************************************
CPU Utilization for 5 seconds = 0%; 1 minute: 3% 5 minutes: 0%

kkasdj-5-1:*************************************************************
CPU Utilization for 5 seconds = 0%; 1 minute: 50% 5 minutes: 0%
    """
    
    mainClusterCpuDict = {}
    text = raw.split("\n\n")
    clusterCpuDict = {}
    for each_line in text:
        cluster_name = re.search(r'Usage Summary In (\w+):',each_line)
        cpu_utilization = re.search(r'1 minute: (\d+)%',each_line)
        
        if cluster_name:
            cluster_name = cluster_name.group(1)
            cpu_utilization_value = cpu_utilization.group(1)
            clusterCpuDict[cluster_name]=cpu_utilization_value
            
        node = re.search(r'^([\w-]+):',each_line, re.MULTILINE)
        node_local = re.search(r'([\w-]+\(.*?\)):', each_line)
        
        if node:
            node_name = node.group(1)
            cpu_utilization_value = cpu_utilization.group(1)
            clusterCpuDict[node_name]=cpu_utilization_value

        if node_local:
            node_local = node_local.group(1)
            cpu_utilization_value = cpu_utilization.group(1)
            clusterCpuDict[node_local]=cpu_utilization_value    
              
    print(clusterCpuDict)
    
    
    
def cluster_conn():
    
    raw = """Usage Summary In Cluster:*********************************************
28 in use, fwd connection 0 in use, dir connection 0 in use, centralized connection 0 in use (Cluster-wide aggregated)

unit-1-1(LOCAL):******************************************************
15 in use, 115 most used, fwd connection 0 in use, 0 most used, dir connection 0 in use, 1 most used, centralized connection 0 in use, 0 most used

unit-2-1:*************************************************************
14 in use, 20 most used, fwd connection 0 in use, 98 most used, dir connection 0 in use, 100 most used, centralized connection 0 in use, 0 most used

"""
    raw = raw.replace(",", "")
    print(raw)
    text = raw.split("\n\n")
    clusterConnDict = {}
    print(len(text))
    print("____________________________")
    print(text)
    for each_line in text:
        cluster_name_match = re.search(r'Usage Summary In Cluster:',each_line)
        connection_in_use_match = re.search(r'(\d+) in use',each_line)
        fwd_conn_match = re.search(r'fwd connection (\d+) in use',each_line)
        dir_conn_match = re.search(r'dir connection (\d+) in use',each_line)
        centralized_conn_match = re.search(r'centralized connection (\d+) in use',each_line)
        
        node_match = re.search(r'^([\w-]+):',each_line, re.MULTILINE)
        node_local_match = re.search(r'([\w-]+\(.*?\)):', each_line)    
            
        if cluster_name_match:
            conn_in_use = connection_in_use_match.group(1)
            fwd_in_use = fwd_conn_match.group(1)
            dirr_in_use = dir_conn_match.group(1)
            centralized_in_use = centralized_conn_match.group(1)
            clu_name = "cluster"
            
            clusterConnDict.update({clu_name:{
                "connections_in_use":conn_in_use,
                "connections_forwarded_in_use":fwd_in_use,
                "connections_direct_in_use":dirr_in_use,
                "connections_centralized_in_use":centralized_in_use}
                })
            
        if node_match and connection_in_use_match and fwd_conn_match and dir_conn_match and centralized_conn_match:
            conn_in_use = connection_in_use_match.group(1)
            fwd_in_use = fwd_conn_match.group(1)
            dirr_in_use = dir_conn_match.group(1)
            centralized_in_use = centralized_conn_match.group(1)
            node = node_match.group(1)
            
            clusterConnDict.update({node:{
                "connections_in_use":conn_in_use,
                "connections_forwarded_in_use":fwd_in_use,
                "connections_direct_in_use":dirr_in_use,
                "connections_centralized_in_use":centralized_in_use}
                })
            
        if node_local_match and connection_in_use_match and fwd_conn_match and dir_conn_match and centralized_conn_match:
            conn_in_use = connection_in_use_match.group(1)
            fwd_in_use = fwd_conn_match.group(1)
            dirr_in_use = dir_conn_match.group(1)
            centralized_in_use = centralized_conn_match.group(1)
            node_local = node_local_match.group(1)
            node_match1 = re.search(r'(.+?)(?=\()',node_local)
            node = node_match1.group(1)
            clusterConnDict.update({node:{
                "connections_in_use":conn_in_use,
                "connections_forwarded_in_use":fwd_in_use,
                "connections_direct_in_use":dirr_in_use,
                "connections_centralized_in_use":centralized_in_use}
                })
                
    print(clusterConnDict)


def cluster_memory():
    
    raw = """Usage Summary In Cluster:*********************************************
Free memory:      54670701192 bytes (77%)
Used memory:      16724408048 bytes (23%)
-------------     ----------------
Total memory:     71395109240 bytes (100%)


unit-1-1(LOCAL):******************************************************
Free memory:      27329899692 bytes (77%)
Used memory:      8367654928 bytes (23%)
-------------     ----------------
Total memory:     35697554620 bytes (100%)


unit-2-1:*************************************************************
Free memory:      27340801500 bytes (77%)
Used memory:      8356753120 bytes (23%)
-------------     ----------------
Total memory:     35697554620 bytes (100%)"""
  
    
    text = dummy(raw)
    print(text)
    clusterMemoryDict = {}
    for each_line in text:
        cluster_name_match, node_match, node_local_match = name(each_line)
        
        match_free_value = re.search(r'Free memory:\s+(\d+)', each_line)
        match_used_value = re.search(r'Used memory:\s+(\d+)', each_line)
        match_total_value = re.search(r'Total memory:\s+(\d+)', each_line)
        
        if match_free_value or match_used_value or match_total_value:
            free_value= match_free_value.group(1)
            used_value = match_used_value.group(1)
            total_value = match_total_value.group(1)
        
        pattern = r"\((\d+)%\)"
        matches = re.findall(pattern, each_line)
        
        free_memory_percentage = matches[0] if len(matches) >= 1 else None
        used_memory_percentage = matches[1] if len(matches) >= 2 else None
        total_memory_percentage = matches[2] if len(matches) >= 3 else None

        if cluster_name_match:
            clusterMemoryDict.update({"cluster":{
                "mem_free_in_bytes":format(int(free_value),"e"),
                "mem_free_in_percentage":free_memory_percentage,
                "mem_total_in_bytes":format(int(total_value),"e"),
                "mem_total_in_percentage":total_memory_percentage,
                "mem_used_in_bytes":format(int(used_value),"e"),
                "mem_used_in_percentage":used_memory_percentage
            }})
            
        if node_match:
            
            node = node_match.group(1)

            clusterMemoryDict.update({node:{
            "mem_free_in_bytes":format(int(free_value),"e"),
            "mem_free_in_percentage":free_memory_percentage,
            "mem_total_in_bytes":format(int(total_value),"e"),
            "mem_total_in_percentage":total_memory_percentage,
            "mem_used_in_bytes":format(int(used_value),"e"),
            "mem_used_in_percentage":used_memory_percentage
        }})
            
        if node_local_match:
            
            node_local = node_local_match.group(1)
            node_match1 = re.search(r'(.+?)(?=\()',node_local)
            node = node_match1.group(1)

            clusterMemoryDict.update({node:{
            "mem_free_in_bytes":format(int(free_value),"e"),
            "mem_free_in_percentage":free_memory_percentage,
            "mem_total_in_bytes":format(int(total_value),"e"),
            "mem_total_in_percentage":total_memory_percentage,
            "mem_used_in_bytes":format(int(used_value),"e"),
            "mem_used_in_percentage":used_memory_percentage
        }})    
            
    print(clusterMemoryDict)
              
def dummy(raw):          
    section_list = []
    current_section = ""
    for line in raw.splitlines():
        if line.strip() == "":
            section_list.append(current_section.strip())
            current_section = ""
        else:
            current_section += line + "\n"
    if current_section.strip() != "":
        section_list.append(current_section.strip())

    # Output the result
    # print(section_list)  
    return section_list
                
def name(s):
    text = s.split("\n\n")
    name_dict = {}
    for each_line in text:
        cluster_name_match = re.search(r'Usage Summary In Cluster:',each_line)
        node_match = re.search(r'^([\w-]+):',each_line, re.MULTILINE)
        node_local_match = re.search(r'([\w-]+\(.*?\)):', each_line)
    return cluster_name_match , node_match, node_local_match  

def cluster_conn_distribution():
    raw = """Unit            Total Rcvd (pkt/sec)    Fwd (pkt/sec)   Locally Processed (%)
unit-1-1            0                   3                   200

unit-2-1            0                   0                   100

"""

    texts = [text for text in raw.splitlines() if text!=""]
    print(texts)
    data = []
    for t in texts:
        data.append(t.split())
    conn_dict = {}
    print(data)
    for i in data[1:]:
        node=i[0]
        packet_total_per_sec = i[1]
        packet_forwarded_per_sec = i[2]
        packet_local_per_sec = i[3]        
        conn_dict.update({node:{
            "packet_total_per_sec":packet_total_per_sec,
            "packet_forwarded_per_sec":packet_forwarded_per_sec,
            "packet_local_per_sec":packet_local_per_sec,
        }})    
    print(conn_dict)
        
def xlate_count():
    
    raw = """Usage Summary In Cluster:*********************************************
1 in use (cluster-wide aggregated)

JHJDSA-1-1(kjdsahfkjfs):******************************************************
4 in use, 2 most used

KJHKJHDSAK-2-1:*************************************************************
6 in use, 2 most used

"""
    xlateDict = {}
    text = [texts for texts in raw.split("\n\n") if texts!=""]
    for each_line in text:
        cluster_name_match = re.search(r'Usage Summary In Cluster:',each_line)
        node_match = re.search(r'^([\w-]+):',each_line, re.MULTILINE)
        node_local_match = re.search(r'([\w-]+\(.*?\)):', each_line)
        
        connection_in_use_match = re.search(r'(\d+) in use',each_line)
        in_use = connection_in_use_match.group(1)
        
        if cluster_name_match:
            cluster_name = "cluster"
            xlateDict.update({cluster_name:{
                "in_use":in_use
            }})
        
        if node_local_match:
            node_local = node_local_match.group(1)
            node_match1 = re.search(r'(.+?)(?=\()',node_local)
            node = node_match1.group(1)
            xlateDict.update({node:{
                "in_use":in_use
            }})
            
        if node_match:
            node = node_match.group(1)   
            xlateDict.update({node:{
                "in_use":in_use
            }})
            
    print(xlateDict)

a = cluster_memory()
