import argparse
from bgpview_io import bgpview_api

def main():
    parser = argparse.ArgumentParser(description="Fetch and display IPv4 prefixes from BGPView API.")
    parser.add_argument("query", type=str, help="Query term for API search")
    args = parser.parse_args()
    
    # fetch and display prefixes
    ipv4_prefixes = bgpview_api.get_ip4_prefixes(args.query)
    print("IPv4 Prefixes:")
    for prefix_info in ipv4_prefixes:
        prefix = prefix_info.get("prefix")
        print(prefix)

if __name__ == "__main__":
    main()