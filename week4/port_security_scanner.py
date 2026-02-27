# SAMPLE DATA

devices = [ 
("192.168.1.10", [22, 80, 443]),
("192.168.1.11", [21, 22, 80]), 
("192.168.1.12", [23, 80, 3389])
]

risky_ports = [21, 23, 3389]

# CODE STARTS HERE
risk_count = {}

for ip, ports in devices:
    for port in ports:
        for risky_port in risky_ports:
            if port == risky_port:
                print( ip + "this shit risky bc of port " + (str(port)))

                # define what ip is in risk_count
                if ip in risk_count:
                    risk_count[ip] = risk_count[ip] + 1
                else:
                    risk_count[ip] = 1

print("Our risk count is: " + str(risk_count))
   
