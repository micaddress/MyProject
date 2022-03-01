{
  "log": {
    "access": "/var/log/v2ray/access.log",
    "error": "/var/log/v2ray/error.log",
    "loglevel": "warning"
  },
  "inbound":{
      "port": 46231,
      "protocol": "vmess",
      "settings": {
        "clients":[
            {
                "id":"",
                "level":1,
                "alterId":32
            }
        ]
      },
      "streamSettings": {
        "network": "kcp",
      },
       "detour":{
           "to": "vmess-detour-151377"
       }
    },
    "outbound":{
        "protocol":"freedom",
        "settings":{}
    },
    "inboundDetour":[
        {
        "protocol":"vmess",
        "port":"40000-50000",
        "tag":"vmess-detour-151377",
        "settings":{},
        "allocate":{
            "strategy":"random",
            "concurrency": 5,
            "refresh":5
        },
        "streamSettings":{
            "network":"kcp"
        }
    },
    {
        "protocol":"shadowsocks",
        "port":443,
        "settings":{
            "method":"chacha20-ietf-poly1305",
            "password":"shadowsocks",
            "udp":true,
            "lecel":1
        }
    }
    ],
    "outboundDetour":[
        {
            "protocol":"blackhole",
            "settings":{},
            "tag":"blocked"
        }
    ],
    "routing":{
        "strategy":"rules",
        "settings":{
            "rules":[
                {
                    "type":"field",
                    "ip":[
                        "0.0.0.0/8",
                        "10.0.0.0/8",
                        "100.64.0.0/10",
                        "127.0.0.0/8",
                        "169.254.0.0/16",
                        "172.16.0.0/12",
                        "192.0.0.0/24",
                        "192.0.2.0/24",
                        "192.168.0.0/16",
                        "198.18.0.0/15",
                        "198.51.100.0/24",
                        "203.0.113.0/24",
                        "::1/128",
                        "fc00::/7",
                        "fe80:/10"
                    ],
                    "outboundTag":"blocked"
                }
            ]
        }
    }
}