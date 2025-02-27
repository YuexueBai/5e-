from data.account import *
from data.image import *
from data.shortcut import *
from data.files import *
from utils.utils import *

window_get('咸鱼喵喵')
n = len(accounts)  # 总应用个数
c = 6  # 每次运行应用的个数
b = 10  # 每个应用能装载的最多账号个数
a = n / c  # 总循环运行次数

i = 0
while i < a:
    # while i < 3:
    h_click(files[i], 0.5)
    j = 0
    while j < b:
        k = 0
        while k < c:
            if accounts_number[i * c + k] > j:
                h_click(shortcuts[i * c + k], 0.5)
                if j > 0:
                    back(0.5)
                    # 资讯浏览
                    click(information, 0.5)
                    click(information, 2)
                    x = 0
                    while x < 3:
                        try:
                            information_click(chat, 0.1)
                            back(0.1)
                        except Exception as e:
                            print(f"浏览资讯失败{e}")
                            pass
                        finally:
                            x += 1
                    # 签到&领取日常任务奖励
                    click(sign_in, 1)
                    g_click(got_it)
                    try:
                        c_click(monthly_reward, 0.5)
                        click(monthly_got, 0.5)
                    except Exception as e:
                        print(f"月常奖励领取失败{e}")
                    click(sign_in_close, 0.5)
                    # 公会分享
                    click(guild, 0.5)
                    click(guild_details, 0.5)
                    click(guild_share, 0.5)
                    gs_click(guild_share_1, 1, guild_details, guild_share)
                    click(web_share, 0.5)
                    back(0.3)
                    back(0.3)
                    # 任务中心&奖励领取
                    click(task_center, 2.5)
                    try:
                        c_click(weekly_reward, 0.5)
                    except Exception as e:
                        print(f"周常奖励领取失败{e}")
                    x = 0
                    while x < 5:
                        try:
                            c_click(guild_task_collect, 1)
                        except Exception as e:
                            print(f"公会任务奖励领取失败{e}")
                            pass
                        finally:
                            x += 1
                    back(0.3)
                    back(0.3)

                # 账号控制
                m_click(mine, 0.5)
                click(settings, 0.5)
                moveto(reference, 0, 0)
                scroll(-400, 1)
                click(switch_accounts, 0.5)
                click(accounts[i * c + k][j], 0.5)
                # 赛事浏览
                click(match, 0.5)
                match_click(match_s, match_s_1, match, 0.5)
                time.sleep(3)
                pyautogui.press('home')
                time.sleep(1)
            k += 1
        if j == 0:
            time.sleep(180 - 10 * (c - 1))
        j += 1
        if j == b:
            k = 0
            while k < c:
                h_click(shortcuts[i * c + k], 0.5)
                back(1)
                # 资讯浏览
                click(information, 0.5)
                click(information, 2)
                x = 0
                while x < 3:
                    try:
                        information_click(chat, 0.1)
                        back(0.1)
                    except Exception as e:
                        print(f"浏览资讯失败{e}")
                        pass
                    finally:
                        x += 1
                # 签到&领取日常任务奖励
                click(sign_in, 1)
                g_click(got_it)
                try:
                    c_click(monthly_reward, 0.5)
                    click(monthly_got, 0.5)
                except Exception as e:
                    print(f"月常奖励领取失败{e}")
                click(sign_in_close, 0.5)
                # 公会分享
                click(guild, 0.5)
                click(guild_details, 0.5)
                click(guild_share, 0.5)
                gs_click(guild_share_1, 1, guild_details, guild_share)
                click(web_share, 0.5)
                back(0.3)
                back(0.3)
                # 任务中心&奖励领取
                click(task_center, 2.5)
                try:
                    c_click(weekly_reward, 0.5)
                except Exception as e:
                    print(f"周常奖励领取失败{e}")
                x = 0
                while x < 5:
                    try:
                        c_click(guild_task_collect, 1)
                    except Exception as e:
                        print(f"公会任务奖励领取失败{e}")
                        pass
                    finally:
                        x += 1
                moveto(logo, 0, 10)
                time.sleep(0.2)
                h_click(close, 1)
                k += 1
    back(0.3)
    back(0.3)
    i += 1
