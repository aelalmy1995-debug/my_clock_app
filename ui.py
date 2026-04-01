from logic import get_time, get_date
from flet import Colors, Column, Container, CrossAxisAlignment, Page, MainAxisAlignment, ProgressRing, Row, Stack, Text, TextStyle, Alignment
import asyncio


FPS = 30
FRAME_TIME = 1 / FPS

async def main(page: Page) -> None:
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.window.prevent_close = True
    page.fonts = {
            "bungee": "/fonts/bungee.ttf",
            "gravitas": "/fonts/gravitas.ttf"
            }
    

    day_display = Text(
            style=TextStyle(
                font_family="bungee",
                size=15,
                color=Colors.DEEP_PURPLE)
            )

    month_display = Text(
            style=TextStyle(
                font_family="bungee",
                size=15,
                color=Colors.DEEP_PURPLE)
            )


    hour_display = Text(
            style=TextStyle(
                font_family="gravitas",
                size=38,
                color=Colors.DEEP_PURPLE)
            )

    minutes_display = Text(
            style=TextStyle(
                font_family="gravitas",
                size=38,
                color=Colors.DEEP_PURPLE)
            )

    progress_sec = ProgressRing(
            value=0,
            width=200,
            height=200,
            stroke_width=10,
            color="#00FFCC")


    progress_ring = Stack(
            width=200,
            height=200,
            controls=[Container(
                content=Column([
                    hour_display,
                    minutes_display,
                    Row([
                        day_display,
                        Text("|", size=25),
                        month_display
                        ],
                        alignment=MainAxisAlignment.CENTER,
                        vertical_alignment=CrossAxisAlignment.CENTER)
                    ],
                               alignment=MainAxisAlignment.CENTER,
                               horizontal_alignment=CrossAxisAlignment.CENTER,
                               spacing=0,
                               margin=20
                               ),
                alignment=Alignment.CENTER
                ),
                      progress_sec,
                      ])


    page.add(progress_ring)


    async def update_time():
        last_min = None
        last_day = None
        last_month = None

        while True:
            t = get_time()
            d = get_date()

            if d['day'] != last_day or d['month'] != last_month:
                day_display.value = d['day']
                month_display.value = d['month']
                last_day = d['day']
                last_month = d['month']
                day_display.update()
                month_display.update()


            if t['minutes'] != last_min:
                hour_display.value = t['hour']
                minutes_display.value = t["minutes"]
                last_min = t['minutes']

                hour_display.update()
                minutes_display.update()

            smooth = t["seconds"] ** 0.85

            progress_sec.value = smooth
            progress_sec.update()


            await asyncio.sleep(FRAME_TIME)


    update_task = asyncio.create_task(update_time())
    
    def on_close(_):
        update_task.cancel()

    page.on_close = on_close
