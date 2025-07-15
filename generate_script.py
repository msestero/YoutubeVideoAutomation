#!/usr/bin/env python3
"""
Simple CLI interface for generating YouTube video scripts
"""

import argparse
import os
from script_generator import VideoScriptGenerator


def main():
    parser = argparse.ArgumentParser(description='Generate YouTube video scripts using ChatGPT')
    
    parser.add_argument('topic', help='The topic for your video')
    parser.add_argument('--length', default='5-10 minutes', help='Expected video length (default: 5-10 minutes)')
    parser.add_argument('--style', default='educational', help='Video style (default: educational)')
    parser.add_argument('--audience', default='general', help='Target audience (default: general)')
    parser.add_argument('--requirements', default='', help='Additional requirements for the script')
    parser.add_argument('--variations', type=int, default=1, help='Number of script variations to generate (default: 1)')
    parser.add_argument('--output', help='Output filename (optional)')
    
    args = parser.parse_args()
    
    try:
        # Initialize generator
        generator = VideoScriptGenerator()
        
        print(f"🎬 Generating script(s) for: {args.topic}")
        print(f"📏 Length: {args.length}")
        print(f"🎭 Style: {args.style}")
        print(f"👥 Audience: {args.audience}")
        
        if args.variations > 1:
            print(f"🔄 Creating {args.variations} variations...")
            
            scripts = generator.generate_multiple_variations(
                topic=args.topic,
                count=args.variations,
                video_length=args.length,
                style=args.style,
                target_audience=args.audience,
                additional_requirements=args.requirements
            )
            
            for i, script in enumerate(scripts, 1):
                filename = generator.save_script(script, 
                    args.output.replace('.', f'_v{i}.') if args.output else None)
                print(f"✅ Variation {i} saved to: {filename}")
        
        else:
            script = generator.generate_script(
                topic=args.topic,
                video_length=args.length,
                style=args.style,
                target_audience=args.audience,
                additional_requirements=args.requirements
            )
            
            filename = generator.save_script(script, args.output)
            print(f"✅ Script saved to: {filename}")
            
            # Show preview
            print("\n" + "="*60)
            print("📝 SCRIPT PREVIEW:")
            print("="*60)
            preview = script['full_script'][:400] + "..." if len(script['full_script']) > 400 else script['full_script']
            print(preview)
            print("="*60)
            print(f"💡 Full script saved to {filename}")
    
    except Exception as e:
        print(f"❌ Error: {e}")
        if "API key" in str(e):
            print("\n🔑 To fix this:")
            print("1. Get an OpenAI API key from https://platform.openai.com/api-keys")
            print("2. Set it as an environment variable:")
            print("   export OPENAI_API_KEY='your-key-here'")
            print("3. Or create a .env file with your API key")


if __name__ == "__main__":
    main()
