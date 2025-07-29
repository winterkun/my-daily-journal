# devPort参数的配置说明

### 问题

devPort 这种参数是在哪里配置的？线上 nginx 还是子应用的 config 文件

### 回答

devPort 这个参数不是在 nginx 或子应用的 config 文件里配置的，而是在**后台管理系统（usms）“前端应用管理” 页面**里配置的。

### 详细说明



1.  **参数含义**：devPort 是每个子应用的 “本地开发端口”，用于主应用在本地开发时通过 local=xxx 参数加载本地子应用。

2.  **配置位置**：在后台管理（usms 系统）→ “前端应用管理” 页面，新增或编辑子应用时，可看到 “本地端口” 字段（即 devPort），直接填写端口号即可。

3.  **参数获取与使用**：该端口号会被主应用通过接口（如 queryAllFrontApps）拉取到，进而用于拼接 //[localhost](https://localhost):devPort 这样的地址。

4.  **与其他配置的区别**：

*   线上 nginx 仅负责转发正式环境的流量，不涉及本地端口的配置。

*   子应用的 config 文件（如 craco.config.js）不会写死端口，本地开发时通常用 .env 或 cross-env PORT=xxxx 方式启动，且端口需和后台配置一致。

### 总结

> devPort 是在后台管理系统配置的，主应用通过接口获取，不在 nginx 或子应用 config 文件里写死。

> （注：文档部分内容可能由 AI 生成）