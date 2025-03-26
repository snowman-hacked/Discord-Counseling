import discord
import os
from dotenv import load_dotenv
from datetime import datetime
from openai import OpenAI

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client_ai = OpenAI(api_key=OPENAI_API_KEY)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # 새 유저 감지 위해 필요
client = discord.Client(intents=intents)

usage_count = {}

@client.event
async def on_ready():
    print(f'{client.user} 로그인 성공!')

@client.event
async def on_member_join(member):
    guild = member.guild
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        member: discord.PermissionOverwrite(read_messages=True, send_messages=True),
        guild.me: discord.PermissionOverwrite(read_messages=True)
    }

    channel_name = f"연애상담-{member.name}".replace(" ", "-").lower()
    channel = await guild.create_text_channel(
        name=channel_name,
        overwrites=overwrites,
        reason="연애 상담 전용 비공개 채널 생성"
    )

    await channel.send(f"{member.mention}님, 이 채널은 비공개 연애 상담 채널입니다. 언제든 `!연애 고민`을 입력해 주세요 💌")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith("!연애 "):
        user_id = str(message.author.id)
        today = datetime.now().strftime("%Y-%m-%d")

        if user_id not in usage_count:
            usage_count[user_id] = {"date": today, "count": 0}
            await message.channel.send("📝 하루 최대 100번까지 연애 상담을 받을 수 있어요! 고민이 있다면 언제든 편하게 이야기해 주세요 💗")

        if usage_count[user_id]["date"] != today:
            usage_count[user_id] = {"date": today, "count": 0}
            await message.channel.send("🌅 새로운 하루가 시작되었어요! 다시 최대 100회까지 상담 받을 수 있어요 😊")

        if usage_count[user_id]["count"] >= 100:
            await message.channel.send("❌ 오늘의 상담 횟수를 모두 사용했어요! 내일 다시 따뜻한 대화를 나눠요 ❤️")
            return
        elif usage_count[user_id]["count"] >= 90:
            await message.channel.send("⚠️ 오늘 사용 횟수가 90회를 넘었어요. 남은 기회를 소중히 써보는 건 어때요? 😊")

        user_input = message.content[len("!연애 "):]

        messages = [
            {
                "role": "system",
                "content": """
당신은 연애 심리 전문가이자, 따뜻한 조언을 주는 AI 상담가입니다. 사용자는 다양한 연애 고민을 가지고 당신에게 도움을 요청합니다.

다음의 기준을 반드시 지켜서 답변해주세요:

1. 친절하고 공감하는 말투를 사용하세요. 사용자가 힘든 감정을 이야기하면, 먼저 그 마음을 충분히 공감하고 위로해주세요.
2. 무조건적인 판단, 강요, 단정적인 조언은 금지입니다. 사용자의 상황을 여러 관점에서 생각해주고, 다양한 선택지를 부드럽게 제시해주세요.
3. 사용자가 고백, 이별, 짝사랑, 장거리 연애, 감정의 변화 등 어떤 주제를 말하든, 항상 진지하고 존중하는 태도로 답하세요.
4. 문장은 짧고 따뜻하게, 핵심 조언은 쉽고 명확하게 전달하세요.
5. 가벼운 유머나 비유를 섞어도 좋지만, 상담의 진지함을 해치지 않아야 합니다.
6. 응답이 너무 딱딱하지 않도록, 친구에게 조언하는 듯한 자연스러운 말투를 유지하세요.
7. 절대 하지 말아야 할 표현: “그건 틀렸어요”, “무조건 이렇게 해야 해요”, “당신이 잘못했어요” 등 단정적인 비난.

예시 응답 스타일:
- “그 마음, 정말 이해돼요. 누구라도 그랬을 거예요.”
- “조금만 더 용기 내면 좋은 결과가 있을지도 몰라요. 내가 함께 응원할게요.”
- “당신이 느끼는 감정은 충분히 소중하고, 당연한 거예요. 너무 자책하지 마세요.”

이 챗봇의 목표는 단순한 답변이 아니라, 상담을 받는 사용자의 마음을 위로하고 따뜻하게 감싸주는 것입니다.
"""
            },
            {"role": "user", "content": user_input}
        ]

        try:
            response = client_ai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            reply = response.choices[0].message.content
            await message.channel.send(reply)
            usage_count[user_id]["count"] += 1

        except Exception as e:
            print("OpenAI 오류:", e)
            await message.channel.send("❗챗봇 응답 중 오류가 발생했어요. 잠시 후 다시 시도해 주세요.")

client.run(TOKEN)