# 项目中URL参数加载本地子应用的实现原理

### 问题

“这个项目是怎么做到，当 url 后面拼接参数 local=ai-escs 的时候，部署的这个项目会加载本地[localhost](https://localhost)的子应用？”

### 实现原理分析



1.  **微前端架构（qiankun）**

*   主应用（如 asmart）通过 qiankun 来加载各个子应用（微应用）。

*   主应用的 src/MicroApps/index.tsx 中，注册和启动微应用时，会根据配置决定每个子应用的加载地址（entry）。

1.  **关键代码**

*   在 packages/asmart/src/MicroApps/index.tsx 中：


    *   `LocationSearch.getURLSearchParam('local')` 会获取当前 URL 中的 local 参数。

    *   `frontApp.code` 是子应用的唯一标识（如 ai-escs）。

    *   `frontApp.devPort` 是该子应用本地开发时的端口（如 18100 等，后台可配置）。

1.  **触发机制**

*   当访问主应用时，URL 后面加上`?local=ai-escs`，例如特定的主应用访问链接。

*   主应用在注册微应用时，发现`local=ai-escs`，且有名为 ai-escs 的子应用，于是把它的 entry 地址设置为`//``localhost``:xxxx`（xxxx 为该子应用的本地端口）。

*   这样 qiankun 就会去加载本地开发环境的子应用，而不是线上部署的版本。

1.  **子应用端口配置**

*   每个子应用的端口（devPort）是在后台管理（如 usms 系统的 “前端应用管理”）里配置的。

*   本地需要启动对应的子应用（如 ai-escs），并保证端口和配置一致。

1.  **总结**

*   只要 URL 带上`local=子应用code`，主应用就会优先加载本地`localhost``:端口`的子应用。

*   这对于本地开发、调试子应用非常方便，无需改主应用代码，只需改 URL 参数即可。

