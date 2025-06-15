# Auto build blog

## Overview

This is an automated blog deployment tool (Version 2.0) designed to simplify the process of setting up and managing a blog using the @sugarat/theme. The tool automates environment setup, blog creation, configuration, and deployment.

## Features

- **Environment Setup**: Automatically checks and installs required software so you don't need to download it yourself just follow the tool:
  - Git
  - Node.js
  - pnpm

- **Blog Management**:
  - Creates new blog projects (with option for custom names)
  - Replaces configuration files
  - Previews the blog locally
  - Builds the blog into a distributable zip file

- **Backup System**: Automatically backs up blog content to a designated location

## Usage

1. Run the script in a Windows environment
2. Follow the interactive prompts to:
   - Set up your development environment
   - Create a new blog project
   - Configure your blog settings
   - Preview or build your blog

### Control Options

During operation, you can choose from these actions:
- `0`: Exit the program
- `1`: Replace blog configuration files
- `2`: Preview the current website
- `3`: Build the current website into a zip package

## Requirements

- Windows operating system
- Internet connection for initial setup

## Author

- **LAnHeNG-**
- Bilibili: [https://space.bilibili.com/2119952581](https://space.bilibili.com/2119952581)
- Blog: [https://lanhengawa.top](https://lanhengawa.top)
- **Clover_233**
- Bilibili: [https://space.bilibili.com/3537124972300357](https://space.bilibili.com/3537124972300357)
- Blog: [https://blog.verr.top](https://blog.verr.top)

## Notes

- The tool automatically creates log files in the `logs` directory
- Configuration is saved in `auto_blog.json`
- Backups are stored in the first available drive under `files_backup` directory (see my blog)

For Linux/MacOS support, check the author's blog for potential updates.

# 博客自动部署工具

## 概述

这是一个自动化博客部署工具（2.0版本），用于简化使用@sugarat/theme搭建和管理博客的流程。该工具可自动完成环境配置、博客创建、设置和部署等操作。

## 功能特点

- **环境自动配置**：自动检测并安装所需软件，无需手动下载：
  - Git版本控制工具
  - Node.js运行环境
  - pnpm包管理器

- **博客管理**：
  - 创建新博客项目（支持自定义项目名）
  - 替换配置文件
  - 本地预览博客效果
  - 将博客构建为可发布的zip压缩包

- **备份系统**：自动将博客内容备份到指定位置

## 使用说明

1. 在Windows环境下运行本脚本
2. 按照交互式提示操作：
   - 配置开发环境
   - 创建博客项目
   - 设置博客配置
   - 预览或构建博客

### 操作选项

运行过程中可选择以下操作：
- `0`：退出程序
- `1`：替换博客配置文件
- `2`：预览当前网站效果
- `3`：将网站构建为zip压缩包

## 系统要求

- Windows操作系统
- 首次使用时需要联网

## 作者信息

- **LAnHeNG-**
- B站主页：[https://space.bilibili.com/2119952581](https://space.bilibili.com/2119952581)
- 个人博客：[https://lanhengawa.top](https://lanhengawa.top)
- **Clover_233**
- B站主页：[https://space.bilibili.com/3537124972300357](https://space.bilibili.com/3537124972300357)
- 个人博客：[https://blog.verr.top](https://blog.verr.top)

## 注意事项

- 工具会自动在`logs`目录下生成日志文件
- 配置信息保存在`auto_blog.json`中
- 备份文件存储在第一个可用磁盘的`files_backup`目录下(磁盘规则见我博客)

如需Linux/MacOS系统支持，请关注作者博客获取可能的更新版本。
