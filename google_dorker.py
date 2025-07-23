import webbrowser
from termcolor import cprint

# List of Google dorks for a specific domain
DORKS = [
    'site:{domain}',
    'site:{domain} intitle:index.of',
    'site:{domain} inurl:admin',
    'site:{domain} inurl:login',
    'site:{domain} inurl:signup',
    'site:{domain} inurl:register',
    'site:{domain} filetype:pdf',
    'site:{domain} filetype:xls OR filetype:xlsx',
    'site:{domain} filetype:doc OR filetype:docx',
    'site:{domain} filetype:sql',
    'site:{domain} ext:xml',
    'site:{domain} ext:conf',
    'site:{domain} ext:log',
    'site:{domain} intext:password',
    'site:{domain} intext:confidential',
    'site:{domain} "login" "admin"',
    'site:{domain} "index of /backup"',
    'site:{domain} "index of /mail"',
    'site:{domain} "index of /private"',
    'site:{domain} "index of /config"',
    'site:{domain} "database dump"',
    'site:{domain} "sql syntax near"',
    'site:{domain} "Warning: mysql_"',
    'site:{domain} "Warning: mysqli_"',
    'site:{domain} "Warning: pg_connect"',
    'site:{domain} "dump.sql"',
    'site:{domain} "env file"',
    'allintext:"{domain}"',
    'intext:"{domain}"',
    'inurl:"{domain}"',
    'allinurl:"{domain}"',
    'intitle:"{domain}"',
    'allintitle:"{domain}"',
    'site:"{domain}"',
    'allinpostauthor:"{domain}"',
    'cache:"{domain}"',
]

def generate_dork_urls(domain):
    base_url = "https://www.google.com/search?q="
    urls = []
    for dork in DORKS:
        query = dork.format(domain=domain)
        full_url = base_url + query.replace(' ', '+')
        urls.append((query, full_url))
    return urls

def main():
    cprint("🕵️ Google Dorking Tool for Specific Domain 🕵️", "cyan", attrs=["bold"])
    domain = input("🔍 Enter the target domain (e.g., example.com): ").strip()
    
    if not domain:
        cprint("❌ No domain entered. Exiting.", "red")
        return

    cprint(f"\n📁 Dorking for domain: {domain}\n", "yellow")

    urls = generate_dork_urls(domain)
    
    for i, (query, url) in enumerate(urls, start=1):
        print(f"[{i:02}] {query}")
        print(f"     🔗 {url}")
    
    open_choice = input("\n🌐 Do you want to open all these in your browser? (y/n): ").strip().lower()
    if open_choice == 'y':
        for _, url in urls:
            webbrowser.open_new_tab(url)
        cprint("✅ URLs opened in your browser.", "green")
    else:
        cprint("📎 URLs generated. You can copy-paste them manually.", "blue")

if __name__ == "__main__":
    main()

