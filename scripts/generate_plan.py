#!/usr/bin/env python3
"""
Validate research JSON and print the output path.
Used as a checkpoint before generating the final plan file.
"""
import json
import sys
import os

def main():
    try:
        data = json.loads(sys.stdin.read())
    except (json.JSONDecodeError, IndexError):
        print("❌ Invalid JSON input", file=sys.stderr)
        sys.exit(1)

    required = ["product_name", "url"]
    missing = [k for k in required if k not in data]
    if missing:
        print(f"❌ Missing fields: {missing}", file=sys.stderr)
        sys.exit(1)

    name_slug = data["product_name"].lower().replace(" ", "-")
    output_path = f"steve_app_ideas/{name_slug}.md"
    print(json.dumps({
        "valid": True,
        "product_name": data["product_name"],
        "output_path": output_path,
        "url": data["url"]
    }))

if __name__ == "__main__":
    main()
