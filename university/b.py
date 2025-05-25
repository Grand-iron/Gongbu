import requests

AI_SERVER_URL = "http://localhost:8000/chat"

# 게임 상태 저장용 딕셔너리
game_state = {
    "gold": 0
}

def get_player_input():
    return input("플레이어 > ")

def send_to_ai_server(message):
    try:
        response = requests.post(AI_SERVER_URL, json={"message": message})
        return response.json().get("response", "오류 발생")
    except:
        return "서버 연결 실패"

def apply_ai_effect(response):
    if "100골드" in response:
        game_state["gold"] += 100
        print("[시스템] 골드 +100 획득!")

def show_ai_response(response):
    print(f"AI > {response}")

def show_player_status():
    print(f"[플레이어 상태] 현재 골드: {game_state['gold']} G")

def main():
    while True:
        user_input = get_player_input()
        if user_input.lower() in ["exit", "quit"]:
            break
        ai_response = send_to_ai_server(user_input)
        apply_ai_effect(ai_response)
        show_ai_response(ai_response)
        show_player_status()

main()
