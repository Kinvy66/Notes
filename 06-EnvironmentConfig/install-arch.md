## 安装 Arch Linux



 ### 网络配置

```bash

iwctl   ## 第一步：进入环境
device list## 第二步：列出网卡设备
station wlan0 scan  ## 第三步：扫描网络，wlan0为无线网卡，wlan0 为无线网卡号
station wlan0 get-networks               ## 第四步：列出扫描到的网络，wlan0 为
station wlan0 connect 网络名称              ## 第五步：连接无线网络，wlan0 为无线网卡
quit   
```



#### 更新系统时间

```bash
timedatectl status
```



### 磁盘分区

- 启动分区 /boot   500MB
- 交换分区   16GB
- 根分区 /   按需分配

查看磁盘

```bash
fdisk -l
```

分区

```bash
fdisk  /dev/sdax
```



格式化

```bash
mkfs.ext4 /dev/root_partition（根分区）
mkswap /dev/swap_partition（交换空间分区）
mkfs.fat -F 32 /dev/efi_system_partition（EFI 系统分区）
```



挂载分区

```bash
mount /dev/root_partition（根分区） /mnt
mkdir /mnt/boot
mount /dev/efi_system_partition（EFI 系统分区）
swapon /dev/swap_partition（交换空间分区）
```



### 安装

修改镜像 `/etc/pacman.d/mirrorlist` 

安装系统

```bash
pacstrap -K /mnt base linux linux-firmware 
```

基础软件

```bash
pacstrap /mnt dhcpcd iwd vim bash-completion sudo
```



用以下命令生成 [fstab](https://wiki.archlinuxcn.org/wiki/Fstab) 文件 (用 `-U` 或 `-L` 选项设置 UUID 或卷标)：

```bash
genfstab -U /mnt >> /mnt/etc/fstab
```





### 配置

进入系统

```bash
arch-chroot /mnt
```

时区

```bash
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
hwclock --systohc    # 同步硬件时钟
```



设置locale

程序和库如果需要本地化文本，都依赖[区域设置](https://wiki.archlinuxcn.org/wiki/Locale)，后者明确规定了地域、货币、时区日期的格式、字符排列方式和其他本地化标准。

需在这两个文件设置：`locale.gen` 与 `locale.conf`。

编辑 `/etc/locale.gen`，然后取消掉 `en_US.UTF-8 UTF-8` 和其他需要的[区域设置](https://wiki.archlinuxcn.org/wiki/Locale)前的注释

接着执行 `locale-gen` 以生成 locale 信息：

```bash
locale-gen
```

然后创建 [locale.conf(5)](https://man.archlinux.org/man/locale.conf.5) 文件，并 [编辑设定 LANG 变量](https://wiki.archlinuxcn.org/wiki/Locale#系统区域设置)，比如：

```
vim /etc/locale.conf
LANG=en_US.UTF-8
```



设置主机名

```bash
vim /etc/hostname
Arch  

```

接下来在`/etc/hosts`设置与其匹配的条目。

```
vim /etc/hosts
```

加入如下内容

```bash
127.0.0.1   localhost
::1         localhost
127.0.1.1   myarch
```



root密码

```bash
passwd 
```

添加普通用户

```bash
useradd -m -G wheel -s /bin/bash kinvy
passwd kinvy
vim /etc/sudoers
# %wheel ALL=(ALL) ALL
```



安装微码

```bash
pacman -S intel-ucode   #Intel
pacman -S amd-ucode     #AMD
```

安装引导

```bash
pacman -S grub efibootmgr   
grub-install --target=x86_64-efi --efi-directory=/efi --bootloader-id=GRUB
grub-mkconfig -o /boot/grub/grub.cfg
```

iwd 

```bash
systemctl start iwd #立即启动iwd
iwctl               #和之前的方式一样，连接无线网络
```





### 桌面环境安装

更新源

```
pacman -Syyu    #升级系统中全部包
```

安装plasma

```bash
pacman -S xorg sddm  xf86-video-intel
pacman -S plasma konsole
systemctl enable sddm
```



