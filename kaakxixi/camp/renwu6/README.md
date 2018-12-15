## 贪吃蛇游戏

2018-12-15 视频地址 https://www.bilibili.com/video/av29129628/

### 注意事项

- 处理🐍身：利用python中的列表存储，吃到食物后，把原来的头插入到snakes的头上即可，使用内置insert方法，同时把snakes最后一个元素删掉，pop即可
- 生成食物：随机生成，但是要注意随机生成的食物位置不要和🐍身重合
- 退出机制：撞墙上或者撞到自己，都退出循环
- pygame三大对象：
  1. pygame.display显示(常见的还有pygame.draw绘制)；
  2. pygame.time时间；
  3. pygame.event事件。
- [pygame实战](https://eyehere.net/tag/pygame/)
