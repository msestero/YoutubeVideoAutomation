#!/usr/bin/env python3
"""
YouTube Video Script Generator using ChatGPT
Automates the creation of video scripts using OpenAI's ChatGPT API
"""

import openai
import json
import os
from datetime import datetime
from typing import Dict, List, Optional


class VideoScriptGenerator:
    def __init__(self, api_key: str = None):
        """Initialize the script generator with OpenAI API key"""
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("OpenAI API key is required. Set OPENAI_API_KEY environment variable or pass it directly.")
        
        openai.api_key = self.api_key
    
    def generate_script(self, 
                       topic: str, 
                       video_length: str = "5-10 minutes",
                       style: str = "educational",
                       target_audience: str = "general",
                       additional_requirements: str = "") -> Dict[str, str]:
        """
        Generate a video script using ChatGPT
        
        Args:
            topic: The main topic/subject of the video
            video_length: Expected length of the video
            style: Style of the video (educational, entertaining, tutorial, etc.)
            target_audience: Target audience description
            additional_requirements: Any additional specific requirements
        
        Returns:
            Dictionary containing the generated script components
        """
        
        prompt = self._build_prompt(topic, video_length, style, target_audience, additional_requirements)
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a professional YouTube script writer who creates engaging, well-structured video scripts."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=2000,
                temperature=0.7
            )
            
            script_content = response.choices[0].message.content
            
            # Parse and structure the response
            script_data = self._parse_script_response(script_content, topic)
            
            return script_data
            
        except Exception as e:
            raise Exception(f"Error generating script: {str(e)}")
    
    def _build_prompt(self, topic: str, video_length: str, style: str, target_audience: str, additional_requirements: str) -> str:
        """Build the ChatGPT prompt for script generation"""
        
        prompt = f"""
Create a YouTube video script with the following specifications:

**Topic**: {topic}
**Video Length**: {video_length}
**Style**: {style}
**Target Audience**: {target_audience}
**Additional Requirements**: {additional_requirements}

Please structure the script with the following sections:

1. **HOOK** (First 15 seconds - grab attention)
2. **INTRODUCTION** (Introduce yourself and the topic)
3. **MAIN CONTENT** (Core content broken into clear sections)
4. **CALL TO ACTION** (Subscribe, like, comment prompts)
5. **OUTRO** (Wrap up and next video tease)

For each section, provide:
- The actual script text
- [Stage directions/notes in brackets]
- Estimated timing

Make the script engaging, conversational, and optimized for YouTube retention. Include natural pauses and emphasis points.
"""
        
        return prompt
    
    def _parse_script_response(self, response: str, topic: str) -> Dict[str, str]:
        """Parse the ChatGPT response into structured script data"""
        
        return {
            "topic": topic,
            "generated_at": datetime.now().isoformat(),
            "full_script": response,
            "hook": self._extract_section(response, "HOOK"),
            "introduction": self._extract_section(response, "INTRODUCTION"),
            "main_content": self._extract_section(response, "MAIN CONTENT"),
            "call_to_action": self._extract_section(response, "CALL TO ACTION"),
            "outro": self._extract_section(response, "OUTRO")
        }
    
    def _extract_section(self, text: str, section_name: str) -> str:
        """Extract a specific section from the script text"""
        try:
            # Simple extraction - look for section headers
            lines = text.split('\n')
            section_lines = []
            in_section = False
            
            for line in lines:
                if section_name.upper() in line.upper() and ('**' in line or '#' in line):
                    in_section = True
                    continue
                elif in_section and ('**' in line or '#' in line) and any(keyword in line.upper() for keyword in ['HOOK', 'INTRODUCTION', 'MAIN', 'CALL', 'OUTRO']):
                    break
                elif in_section:
                    section_lines.append(line)
            
            return '\n'.join(section_lines).strip()
        except:
            return "Section not found"
    
    def save_script(self, script_data: Dict[str, str], filename: str = None) -> str:
        """Save the generated script to a file"""
        
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            safe_topic = "".join(c for c in script_data['topic'] if c.isalnum() or c in (' ', '-', '_')).rstrip()
            filename = f"script_{safe_topic.replace(' ', '_')}_{timestamp}.json"
        
        # Save as JSON
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(script_data, f, indent=2, ensure_ascii=False)
        
        # Also save as readable text
        text_filename = filename.replace('.json', '.txt')
        with open(text_filename, 'w', encoding='utf-8') as f:
            f.write(f"YouTube Video Script: {script_data['topic']}\n")
            f.write(f"Generated: {script_data['generated_at']}\n")
            f.write("=" * 50 + "\n\n")
            f.write(script_data['full_script'])
        
        return filename
    
    def generate_multiple_variations(self, topic: str, count: int = 3, **kwargs) -> List[Dict[str, str]]:
        """Generate multiple script variations for the same topic"""
        
        variations = []
        for i in range(count):
            try:
                script = self.generate_script(topic, **kwargs)
                script['variation'] = i + 1
                variations.append(script)
            except Exception as e:
                print(f"Error generating variation {i+1}: {e}")
        
        return variations


def main():
    """Example usage of the script generator"""
    
    # Initialize the generator
    try:
        generator = VideoScriptGenerator()
    except ValueError as e:
        print(f"Error: {e}")
        print("Please set your OpenAI API key as an environment variable:")
        print("export OPENAI_API_KEY='your-api-key-here'")
        return
    
    # Example script generation
    topic = "How to Start a YouTube Channel in 2024"
    
    print(f"Generating script for: {topic}")
    
    try:
        script = generator.generate_script(
            topic=topic,
            video_length="8-10 minutes",
            style="educational and motivational",
            target_audience="aspiring YouTubers and content creators",
            additional_requirements="Include practical tips and current YouTube algorithm insights"
        )
        
        # Save the script
        filename = generator.save_script(script)
        print(f"Script saved to: {filename}")
        
        # Display preview
        print("\n" + "="*50)
        print("SCRIPT PREVIEW:")
        print("="*50)
        print(script['full_script'][:500] + "...")
        
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
