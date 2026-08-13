import json
import os
import streamlit as st
from streamlit.components.v1 import html as html_component

st.set_page_config(
    page_title="The Little Leprechaun",
    page_icon=":four_leaf_clover:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

HERE = os.path.dirname(os.path.abspath(__file__))


def resolve_book_dir():
    candidates = [
        os.environ.get("LEPRECHAUN_BOOK_DIR", ""),
        st.secrets.get("BOOK_DIR", ""),
        os.path.join(HERE, "images"),
        r"E:\Books\The Little Leprechaun",
    ]
    for c in candidates:
        if c and os.path.isdir(c):
            return c
    return candidates[-1]


BOOK_DIR = resolve_book_dir()

PAGES = [
    {
        "image": "page_1.png",
        "title": "The Little Leprechaun",
        "narration": (
            "The Little Leprechaun. A bedtime story for the young and young at heart. "
            "By Adam Molden."
        ),
        "fact": None,
    },
    {
        "image": "page_2.png",
        "title": "Dedication",
        "narration": (
            "I once asked my grandfather why the stars look silver and where they come from. "
            "This book is dedicated to his memory."
        ),
        "fact": None,
    },
    {
        "image": "page_3.png",
        "title": "Intro",
        "narration": (
            "My grandfather was born in a different time. He was a storyteller. "
            "All of our recorded history was once handed down from generation to generation "
            "with storytelling, he would say to me. He was also mostly Irish and loved to "
            "make up stories, so I took most of what he said with a light heart."
        ),
        "fact": None,
    },
    {
        "image": "page_4.png",
        "title": "The Little Leprechaun",
        "narration": (
            "A long time ago, before the night sky was what you see tonight, there were the "
            "wee little people. They lived in a magical place called Hibernia. Today, we call "
            "this place Ireland, and the magical people are called leprechauns."
        ),
        "fact": (
            "Hibernia is the old Latin name for Ireland. It is also called the Emerald Isle "
            "because of its green hills!"
        ),
    },
    {
        "image": "page_5.png",
        "title": "No Stars?",
        "narration": (
            "As many people already know, leprechauns love their pots of gold and hide them "
            "at the end of rainbows. What many do not know is... silver was the leprechaun's "
            "favorite metal before gold. In fact, they had a large machine way far away in "
            "the dark night sky for making silver coins."
        ),
        "fact": "Legend says you can find a pot of gold at the end of a rainbow!",
    },
    {
        "image": "page_6.png",
        "title": "The Machine",
        "narration": (
            "Every night, they would fly up to the machine and make their silver coins. "
            "The gigantic machine was silver and round like a soccer ball. It was so big it "
            "could even be seen from the ground."
        ),
        "fact": None,
    },
    {
        "image": "page_7.png",
        "title": "The Big Reveal",
        "narration": (
            "That big silver ball in the night sky? We now call it the moon. The machine was "
            "so big, the only way to hide it was in plain sight. The leprechauns are crafty "
            "people."
        ),
        "fact": (
            "The real moon is about 384,400 kilometres away. That is a very long walk!"
        ),
        "interaction": "wave",
    },
    {
        "image": "page_8.png",
        "title": "The Nightly Task",
        "narration": (
            "So every night, to be sure no one would steal their silver, they would send one "
            "lucky leprechaun to the moon to mint silver coins. It was a great honor to be "
            "chosen for taking on such a task."
        ),
        "fact": None,
    },
    {
        "image": "page_9.png",
        "title": "A Lucky Problem",
        "narration": (
            "Now every generation of the leprechauns has one which is not blessed with the "
            "best of luck. This is especially unfortunate because the leprechauns are known "
            "throughout the mythical realms for their luck."
        ),
        "fact": None,
    },
    {
        "image": "page_10.png",
        "title": "The Littlest Leprechaun",
        "narration": (
            "This story is of one who not only had bad luck but also was very short in "
            "stature, even for little folk. He was the littlest leprechaun. It just so "
            "happened he was accident-prone as well. Our littlest of the little people's "
            "name was Mani."
        ),
        "fact": None,
    },
    {
        "image": "page_11.png",
        "title": "Mani Flies to the Moon",
        "narration": (
            "Mani was very eager to prove himself to the whole clan. He had never been chosen "
            "for the nightly task for obvious reasons. So one night, before the official "
            "leprechaun was chosen, Mani grabbed the pot of raw liquid silver and flew to the "
            "moon. Mani did have one special talent: he was fast!"
        ),
        "fact": None,
    },
    {
        "image": "page_12.png",
        "title": "A Green Blur",
        "narration": (
            "He made silver coins faster than anyone has ever made. His hands were moving so "
            "quick over the controls on the machine you could barely see them. He was moving "
            "with such speed he looked like a green blur. Mani had made it through half of "
            "the silver pot at record speed when he tripped..."
        ),
        "fact": None,
    },
    {
        "image": "page_13.png",
        "title": "And That's How the Stars Were Made!",
        "narration": (
            "He fell right into the pot of liquid silver and splashed the silver out of the "
            "pot. Since he was moving so fast, the silver splashed out into the night sky and "
            "went everywhere. That is how the stars in the night were created! "
            "It was so beautiful the leprechauns were not mad at Mani. They asked him to stay "
            "on the moon and watch over his amazing creation. This is also one of the reasons "
            "leprechauns switched to gold. And if you look closely at the moon, you can still "
            "see Mani up there in the night sky. He is known as the man in the moon. "
            "The End!"
        ),
        "fact": None,
        "interaction": "sprinkle",
    },
]


def css():
    st.markdown(
        """
        <style>
            .stApp {
                background: radial-gradient(ellipse at top, #1b2450 0%, #0c1030 55%, #06081c 100%);
                color: #eef0ff;
            }
            .block-container { padding-top: 1.5rem; }
            .book-title {
                font-family: Georgia, 'Times New Roman', serif;
                background: linear-gradient(90deg, #ffd76e, #ffb14e, #ffd76e);
                -webkit-background-clip: text;
                background-clip: text;
                color: transparent;
                font-weight: 700;
                letter-spacing: 1px;
            }
            .page-caption {
                color: #c7cdf5;
                font-family: Georgia, serif;
                font-style: italic;
                text-align: center;
                margin-top: 0.35rem;
            }
            .fact-box {
                background: rgba(255, 215, 110, 0.10);
                border: 1px solid rgba(255, 215, 110, 0.35);
                border-radius: 14px;
                padding: 0.75rem 1rem;
                color: #ffe9b8;
                font-family: Georgia, serif;
            }
            .nav-hint { color: #9aa0d4; font-size: 0.85rem; }
            div[data-testid="stButton"] button {
                background: rgba(255, 215, 110, 0.12);
                border: 1px solid #ffd76e;
                color: #ffd76e;
                border-radius: 999px;
                font-weight: 600;
            }
            div[data-testid="stButton"] button:hover {
                background: rgba(255, 215, 110, 0.28);
                color: #fff3d0;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def speak(text):
    safe = json.dumps(text)
    html_component(
        f"""
        <script>
            window.parent.postMessage({{type:"streamlit:speak", text:{safe}}}, "*");
            const msg = new SpeechSynthesisUtterance({safe});
            msg.rate = 0.85;
            msg.pitch = 1.05;
            speechSynthesis.cancel();
            speechSynthesis.speak(msg);
        </script>
        """,
        height=0,
    )


def star_sprinkle():
    html_component(
        """
        <style>
          .sky { position: relative; height: 180px; width: 100%; overflow: hidden;
                 border-radius: 14px;
                 background: radial-gradient(ellipse at bottom, #2a1a5e 0%, #0b0e33 70%); }
          .star { position: absolute; border-radius: 50%; background: #fff3c4;
                  animation: twinkle 1.4s ease-in-out infinite, fall 3s linear infinite; }
          @keyframes twinkle {
            0%,100% { opacity: 0.25; transform: scale(0.7); }
            50%     { opacity: 1;   transform: scale(1.25); }
          }
          @keyframes fall {
            0%   { transform: translateY(-10px); }
            100% { transform: translateY(190px); }
          }
        </style>
        <div class="sky" id="sky"></div>
        <script>
          const sky = document.getElementById('sky');
          const colors = ['#fff3c4', '#dfe7ff', '#ffd76e', '#ffffff'];
          for (let i = 0; i < 45; i++) {
            const s = document.createElement('div');
            s.className = 'star';
            const size = 3 + Math.random() * 5;
            s.style.width = size + 'px';
            s.style.height = size + 'px';
            s.style.left = Math.random() * 100 + '%';
            s.style.top = Math.random() * 100 + '%';
            s.style.background = colors[Math.floor(Math.random() * colors.length)];
            s.style.animationDelay = (Math.random() * 2) + 's, ' + (Math.random() * 3) + 's';
            sky.appendChild(s);
          }
          try {
            const ctx = new AudioContext();
            for (let i = 0; i < 8; i++) {
              const o = ctx.createOscillator();
              const g = ctx.createGain();
              o.frequency.value = 880 + i * 220;
              o.connect(g); g.connect(ctx.destination);
              g.gain.setValueAtTime(0.0001, ctx.currentTime + i * 0.08);
              g.gain.exponentialRampToValueAtTime(0.08, ctx.currentTime + i * 0.08 + 0.02);
              g.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + i * 0.08 + 0.7);
              o.start(ctx.currentTime + i * 0.08);
              o.stop(ctx.currentTime + i * 0.08 + 0.8);
            }
          } catch (e) {}
        </script>
        """,
        height=190,
    )


def make_mani_wave():
    html_component(
        """
        <style>
          .wave-box { height: 70px; display: flex; align-items: center; justify-content: center;
                      font-size: 1.5rem; gap: 0.5rem; }
          .mani { display: inline-block; animation: bounce 0.6s ease-in-out 3; }
          @keyframes bounce {
            0%,100% { transform: translateY(0) rotate(0deg); }
            50%     { transform: translateY(-14px) rotate(-8deg); }
          }
        </style>
        <div class="wave-box">
          <span style="color:#c9d2ff; font-family: Georgia, serif;">Shhh... that's Mani up there! &#127769;</span>
          <span class="mani" style="font-size:2rem;">&#127807;</span>
          <span class="mani" style="font-size:2rem;">&#128075;</span>
        </div>
        <script>
          try {
            const ctx = new AudioContext();
            const o = ctx.createOscillator();
            const g = ctx.createGain();
            o.frequency.value = 523;
            o.connect(g); g.connect(ctx.destination);
            g.gain.setValueAtTime(0.001, ctx.currentTime);
            g.gain.exponentialRampToValueAtTime(0.09, ctx.currentTime + 0.02);
            g.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + 0.9);
            o.start(); o.stop(ctx.currentTime + 1);
          } catch (e) {}
        </script>
        """,
        height=80,
    )


def main():
    css()

    if "page" not in st.session_state:
        st.session_state.page = 0

    total = len(PAGES)
    idx = st.session_state.page
    page = PAGES[idx]

    top_left, top_right = st.columns([3, 1])
    with top_left:
        st.markdown("<h1 class='book-title'>\u2726 The Little Leprechaun \u2726</h1>",
                    unsafe_allow_html=True)
    with top_right:
        st.markdown(
            f"<div style='text-align:right; color:#9aa0d4;'>"
            f"Page {idx + 1} of {total}</div>",
            unsafe_allow_html=True,
        )

    st.progress((idx + 1) / total)

    nav_top = st.columns([1, 4, 1])
    with nav_top[0]:
        if st.button("\u25c0 Back", key="back_top", disabled=idx == 0,
                     use_container_width=True):
            st.session_state.page -= 1
            st.rerun()
    with nav_top[2]:
        if st.button("Next \u25b6", key="next_top", disabled=idx == total - 1,
                     use_container_width=True):
            st.session_state.page += 1
            st.rerun()

    st.markdown(f"<p class='page-caption'>{page['title']}</p>", unsafe_allow_html=True)

    img_path = os.path.join(BOOK_DIR, page["image"])
    if os.path.exists(img_path):
        st.image(img_path, use_container_width=True)
    else:
        st.error(
            f"Could not find {page['image']}. Searched in `{BOOK_DIR}`. "
            "Set the LEPRECHAUN_BOOK_DIR env var (or BOOK_DIR in secrets) "
            "to the folder containing the page images."
        )

    mid = st.columns([1, 4, 1])
    with mid[1]:
        if st.button("\U0001f4d6 Listen to this page", key="listen",
                     use_container_width=True):
            speak(page["narration"])

    if page.get("interaction") == "wave":
        if st.button("\U0001f44b Make Mani wave!", key="wave",
                     use_container_width=True):
            make_mani_wave()
    elif page.get("interaction") == "sprinkle":
        if st.button("\u2728 Sprinkle the stars! \u2728", key="sprinkle",
                     use_container_width=True):
            star_sprinkle()

    if page.get("fact"):
        st.markdown(
            f"<div class='fact-box'>&#11088; <b>Did you know?</b> {page['fact']}</div>",
            unsafe_allow_html=True,
        )

    with st.expander("Story text (for parents / read-along)"):
        st.markdown(page["narration"])

    with st.expander("Parents' corner \u2014 how to use this app"):
        st.markdown(
            "Use the <b>Back</b> and <b>Next</b> buttons (or the arrows at the top) to turn "
            "the pages. <b>Listen to this page</b> reads the story aloud using your device's "
            "text-to-speech. Keep an eye out for <b>special buttons</b> \u2014 Mani has a "
            "couple of surprises hidden in the story!"
        )

    nav_bottom = st.columns([1, 4, 1])
    with nav_bottom[0]:
        if st.button("\u25c0 Back", key="back_bot", disabled=idx == 0,
                     use_container_width=True):
            st.session_state.page -= 1
            st.rerun()
    with nav_bottom[1]:
        st.markdown(
            f"<div class='nav-hint' style='text-align:center;'>"
            f"{idx + 1} / {total} \u00b7 by Adam Molden</div>",
            unsafe_allow_html=True,
        )
    with nav_bottom[2]:
        if st.button("Next \u25b6", key="next_bot", disabled=idx == total - 1,
                     use_container_width=True):
            st.session_state.page += 1
            st.rerun()


if __name__ == "__main__":
    main()
