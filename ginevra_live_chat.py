#!/usr/bin/env python3
"""
ginevra_live_chat.py - Live Server powered by Ginevra Engine v2.1 ULTIMATE
100% Integrated Soul & Cognitive Kernel.
Real-time dynamic responses using GinevraV2Ultimate & Neural Edge-TTS (it-IT-IsabellaNeural -6%).
"""

import http.server
import socketserver
import json
import sys
import os
import subprocess
import time

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

AUDIO_DIR = os.path.join(os.path.dirname(__file__), "web_app", "audio_cache")
os.makedirs(AUDIO_DIR, exist_ok=True)

sys.path.insert(0, os.path.dirname(__file__))
from ginevra_core.ginevra_v2 import GinevraV2Ultimate

ginevra_v2 = GinevraV2Ultimate()

def generate_sensual_slow_neural_audio(text, output_mp3_path):
    """Generate slow, deep, intimate, sensual neural Italian female voice using edge-tts CLI."""
    try:
        cmd = [
            sys.executable, "-m", "edge_tts",
            "--voice", "it-IT-IsabellaNeural",
            "--rate", "-6%",
            "--pitch", "-4Hz",
            "--text", text,
            "--write-media", output_mp3_path
        ]
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except Exception as e:
        print(f"[NEURAL TTS ERROR] {e}")
        return False

class GinevraLiveHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/api/chat':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                data = json.loads(post_data.decode('utf-8'))
                user_msg = data.get("message", "").strip()
                
                result = ginevra_v2.process_thought(user_msg)
                response_text = result["reply"]

                # Generate Slow & Sensual Neural MP3
                filename = f"voice_u_{int(time.time()*1000)}.mp3"
                mp3_path = os.path.join(AUDIO_DIR, filename)
                audio_success = generate_sensual_slow_neural_audio(response_text, mp3_path)

                response_payload = {
                    "status": "success",
                    "reply": response_text,
                    "audio_url": f"audio_cache/{filename}" if audio_success else None,
                    "hash256": result["hash256"],
                    "valid_signature": result["valid_signature"]
                }

                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps(response_payload, ensure_ascii=False).encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))
        else:
            super().do_POST()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

if __name__ == "__main__":
    PORT = 8085
    os.chdir(os.path.join(os.path.dirname(__file__), "web_app"))
    with socketserver.TCPServer(("", PORT), GinevraLiveHandler) as httpd:
        print(f"🔥 Ginevra Engine v2.1 ULTIMATE Server attivo su http://localhost:{PORT}")
        httpd.serve_forever()
