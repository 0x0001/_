import urllib.request

# https://raw.githubusercontent.com/Aethersailor/Custom_OpenClash_Rules/main/cfg/Custom_Clash.ini
direct = [
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Lan/Lan.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Direct/Direct.list",
    "https://raw.githubusercontent.com/Aethersailor/Custom_OpenClash_Rules/main/rule/Custom_Direct.list",
    "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ChinaDomain.list",
    "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ChinaCompanyIp.list",
    "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ChinaIp.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Download/Download.list",
    "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/GoogleCN.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/SteamCN/SteamCN.list",
    "https://raw.githubusercontent.com/Aethersailor/Custom_OpenClash_Rules/main/rule/Steam_CDN.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/PrivateTracker/PrivateTracker.list",
]

proxy = [
    "https://raw.githubusercontent.com/Aethersailor/Custom_OpenClash_Rules/main/rule/Custom_Proxy.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/GoogleFCM/GoogleFCM.list", # 谷歌FCM
    "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Ruleset/GoogleCNProxyIP.list",
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Telegram/Telegram.list", # Telegram
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/OpenAI/OpenAI.list", # OpenAI
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Copilot/Copilot.list", # Copilot
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/GitHub/GitHub.list", # GitHub
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/YouTube/YouTube.list", # YouTube
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Google/Google.list", # Google
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/TikTok/TikTok.list", # TikTok
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Netflix/Netflix.list", # Netflix
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Disney/Disney.list", # Disney
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Spotify/Spotify.list",# Spotify
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Bahamut/Bahamut.list", # Bahamut
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/GlobalMedia/GlobalMedia.list", # GlobalMedia
    "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ProxyGFWlist.list", 
]

def get(url:str):
    try:
        response = urllib.request.urlopen(url)
        if response.getcode() == 200:
            return response.read().decode('utf-8')
        else:
            return None
    except Exception as e:
        print(e)
        return None

def merge(url_list: list[str])-> str:
    contents = set()
    for u in url_list:
        content = get(u)
        if content:
            lines = content.split('\n')
            lines = [line.strip() for line in lines if line.strip() and not line.strip().startswith('#')]
            contents.update(lines)
    # sort
    contents = sorted(contents)
    if contents:
        return '\n'.join(contents) or ''
    return ''

def main():
    direct_content = merge(direct)
    with open('./Custom_Direct.list', 'w', encoding='utf-8') as f:
        f.write(direct_content)

    proxy_content = merge(proxy)
    with open('./Custom_Proxy.list', 'w', encoding='utf-8') as f:
        f.write(proxy_content)

if __name__ == '__main__':
    main()
