#!/usr/bin/env python3
"""
Research a competitor product from a given URL.

Usage:
    python scripts/research_competitor.py --url https://competitor.com

Output:
    JSON dict with: name, description, pricing, features, flow_steps,
    target_market, social_proof, moats, tech_notes
"""
import json
import sys
import re
from urllib.parse import urlparse

def extract_domain(url):
    """Extract clean domain name from URL."""
    parsed = urlparse(url)
    domain = parsed.netloc or parsed.path
    domain = re.sub(r'^www\.', '', domain)
    return domain.split('.')[0].capitalize()

def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--url':
        url = sys.argv[2]
    else:
        url = input("Enter competitor URL: ").strip()

    product_name = extract_domain(url)

    # Output template for the next stage
    result = {
        "product_name": product_name,
        "url": url,
        "status": "research_ready"
    }

    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
