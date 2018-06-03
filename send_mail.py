import os
from django.core.mail import send_mail,EmailMultiAlternatives

# 另外，由于我们是单独运行send_mail.py文件，所以无法使用Django环境，需要通过os模块对环境变量进行设置，也就是：
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':

    # send_mail(
    #     '来自www.gxyblog.com的测试邮件',
    #     '欢迎访问www.gxyblog.com 这里是高欣怡的博客和教程站点，本站专注于python和django开发',
    #     '18362208991@163.com',
    #     ['352175516@qq.com'],
    #     # 对于send_mail方法，第一个参数是邮件主题subject；第二个参数是邮件具体内容；第三个参数是邮件发送方，需要和你settings中的一致；第四个参数是接受方的邮件地址列表。请按你自己实际情况修改发送方和接收方的邮箱地址
    # )

    subject, from_email, to = '来自www.gxyblog.com的测试邮件', '18362208991@163.com', '352175516@qq.com'
    text_content = '欢迎访问www.liujiangblog.com，这里是刘江的博客和教程站点，专注于Python和Django技术的分享！'
    html_content = '<p>欢迎访问<a href="http://www.liujiangblog.com" target=blank>www.liujiangblog.com</a>，这里是刘江的博客和教程站点，专注于Python和Django技术的分享！</p>'
    msg = EmailMultiAlternatives(subject, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()