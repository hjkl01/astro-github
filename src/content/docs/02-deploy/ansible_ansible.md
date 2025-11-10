---
title: ansible
---


# Ansible

**GitHub项目地址**: https://github.com/ansible/ansible

## 主要特性

- **无代理（Agentless）**：通过 SSH、WinRM 等协议直接在目标主机上执行任务，无需在目标节点安装任何代理软件。  
- **声明式配置**：使用 YAML 编写 Playbook，描述期望的系统状态，Ansible 自动完成差异比较并执行必要的操作。  
- **模块化**：内置数百个模块（如 `apt`, `yum`, `service`, `file`, `git`, `template` 等），可一次性执行多种操作。  
- **角色（Roles）**：将 Playbook、任务、变量、文件、模板等组织为可复用的单元，便于团队协作与代码复用。  
- **可扩展性**：支持自定义模块、插件、过滤器等，满足复杂业务需求。  
- **安全性**：支持 SSH 密钥、密钥管理、Vault 加密、权限最小化等安全特性。  
- **多平台支持**：兼容 Linux、macOS、Windows、网络设备、云服务等多种目标环境。  
- **并行执行**：默认并行执行，支持可配置并发数，提升部署效率。

## 核心功能

| 功能 | 说明 |
|------|------|
| **Playbook** | 用 YAML 编写的任务集合，定义 hosts、tasks、vars、handlers 等。 |
| **Inventory** | 以 INI、YAML、脚本或动态方式描述目标主机和主机组。 |
| **Ad‑hoc 命令** | `ansible <host_pattern> -m <module> -a "<args>"` 用于快速执行一次性任务。 |
| **Roles** | 结构化目录（tasks, handlers, defaults, vars, files, templates）支持重复使用。 |
| **Vault** | 加密敏感数据（密码、密钥等），在 Playbook 运行时解密。 |
| **Callbacks & Plugins** | 可自定义输出格式、日志、事件处理等。 |
| **Dynamic Inventory** | 通过脚本或云平台 API 自动生成 inventory。 |

## 使用方法

1. **安装**  
   ```bash
   pip install ansible
   ```
   或使用系统包管理器（如 `apt install ansible`）。

2. **编写 Inventory**  
   ```ini
   [web]
   web01.example.com
   web02.example.com

   [db]
   db01.example.com
   ```

3. **编写 Playbook**  
   ```yaml
   - hosts: web
     become: yes
     tasks:
       - name: 安装 Nginx
         apt:
           name: nginx
           state: present
       - name: 启动 Nginx
         service:
           name: nginx
           state: started
   ```

4. **执行 Playbook**  
   ```bash
   ansible-playbook -i hosts.ini site.yml
   ```

5. **使用角色**  
   ```bash
   ansible-galaxy init my_role
   ```
   在 `my_role/tasks/main.yml` 写任务，随后在 Playbook 引用：
   ```yaml
   - hosts: all
     roles:
       - my_role
   ```

6. **加密变量**  
   ```bash
   ansible-vault encrypt_string 'mysecret' --name 'db_password'
   ```
   在 Playbook 中引用 `{{ db_password }}`。

7. **动态 Inventory 示例**（AWS EC2）  
   ```bash
   ansible-galaxy collection install amazon.aws
   ansible-inventory --graph
   ```

> 详细文档请参阅官方文档: https://docs.ansible.com/

--- 
```
