### Описание проекта  
Проект представляет собой инструмент командной строки для визуализации графов зависимостей пакетов Ubuntu, включая транзитивные зависимости. Граф зависимостей формируется в формате Mermaid.

---

### Функциональность
**Основные функции:**

-Анализ графа зависимостей указанного пакета.

-Транзитивный анализ зависимостей с ограничением глубины.

-Вывод графа зависимостей в формате Mermaid.

-Генерация SVG-изображения графа.

**Гибкая конфигурация:**

-Задание пути к утилите визуализации графов.

-Настройка глубины анализа зависимостей.

-Выбор файла для сохранения результата.

**Поддержка формата Mermaid:**

-Генерация графов в формате Mermaid для визуализации.

**Тестирование:**

-Все функции инструмента покрыты тестами, включая обработку исключений.

---

### Установка и запуск

#### Установка зависимостей
Убедитесь, что у вас установлен Python версии 3.8+ и выполните:  
```bash
pip install -r requirements.txt
```

#### Запуск программы  
Для запуска эмулятора выполните следующую команду:  
```bash
python visualizer.py --path <путь_к_mermaid_CLI> --package <имя_пакета> --repo <url_репозитория> --output <путь_к_SVG_файлу> --max-depth <максимальная_глубина>
```

Пример:  
```bash
python visualizer.py --path ./mmdc --package obsession --repo http://archive.ubuntu.com/ubuntu/pool/universe/ --output obsession_graph.svg --max-depth 2
```
---
## Формат данных

 Формат Mermaid

 Граф зависимостей сохраняется в формате Mermaid. Пример:
 ```bash
flowchart TD;
    id1["package1"] --> id2["dependency1"];
    id1 --> id3["dependency2"];
    id2 --> id4["dependency3"];

```

SVG-результат

Результат визуализации сохраняется в SVG-файле. Пример содержимого:
```bash
<svg xmlns="http://www.w3.org/2000/svg" ...>
    <!-- Граф в формате SVG -->
</svg>

```
---
## Зависимости
Для работы инструмента требуются следующие зависимости:
```bash
beautifulsoup4==4.13.0
requests==2.31.0
pytest==8.3.3
lxml==4.9.3

```
---
## Тестирование
Для запуска тестов выполните:
```bash
pytest
```
---

## Пример работы
1.Генерация Mermaid-кода:
```bash
flowchart TD;
	id0["obsession"] --> id1["debhelper(>=9)"];
	id0["obsession"] --> id2["libglib2.0-dev"];
	id0["obsession"] --> id3["libdbus-1-dev"];
	id0["obsession"] --> id4["libx11-dev"];
	id0["obsession"] --> id5["libgtk2.0-dev"];
	id0["obsession"] --> id6["valac"];
```

2.SVG-визуализация:
![image](https://github.com/user-attachments/assets/e5abb8d8-1afd-4dd9-b0bc-07b1db942427)
```bash
<svg aria-roledescription="flowchart-v2" role="graphics-document document" viewBox="0 0 1137.125 174" style="max-width: 1137.12px; background-color: white;" class="flowchart" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" width="100%" id="my-svg"><style>#my-svg{font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:16px;fill:#333;}#my-svg .error-icon{fill:#552222;}#my-svg .error-text{fill:#552222;stroke:#552222;}#my-svg .edge-thickness-normal{stroke-width:1px;}#my-svg .edge-thickness-thick{stroke-width:3.5px;}#my-svg .edge-pattern-solid{stroke-dasharray:0;}#my-svg .edge-thickness-invisible{stroke-width:0;fill:none;}#my-svg .edge-pattern-dashed{stroke-dasharray:3;}#my-svg .edge-pattern-dotted{stroke-dasharray:2;}#my-svg .marker{fill:#333333;stroke:#333333;}#my-svg .marker.cross{stroke:#333333;}#my-svg svg{font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:16px;}#my-svg p{margin:0;}#my-svg .label{font-family:"trebuchet ms",verdana,arial,sans-serif;color:#333;}#my-svg .cluster-label text{fill:#333;}#my-svg .cluster-label span{color:#333;}#my-svg .cluster-label span p{background-color:transparent;}#my-svg .label text,#my-svg span{fill:#333;color:#333;}#my-svg .node rect,#my-svg .node circle,#my-svg .node ellipse,#my-svg .node polygon,#my-svg .node path{fill:#ECECFF;stroke:#9370DB;stroke-width:1px;}#my-svg .rough-node .label text,#my-svg .node .label text,#my-svg .image-shape .label,#my-svg .icon-shape .label{text-anchor:middle;}#my-svg .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#my-svg .rough-node .label,#my-svg .node .label,#my-svg .image-shape .label,#my-svg .icon-shape .label{text-align:center;}#my-svg .node.clickable{cursor:pointer;}#my-svg .root .anchor path{fill:#333333!important;stroke-width:0;stroke:#333333;}#my-svg .arrowheadPath{fill:#333333;}#my-svg .edgePath .path{stroke:#333333;stroke-width:2.0px;}#my-svg .flowchart-link{stroke:#333333;fill:none;}#my-svg .edgeLabel{background-color:rgba(232,232,232, 0.8);text-align:center;}#my-svg .edgeLabel p{background-color:rgba(232,232,232, 0.8);}#my-svg .edgeLabel rect{opacity:0.5;background-color:rgba(232,232,232, 0.8);fill:rgba(232,232,232, 0.8);}#my-svg .labelBkg{background-color:rgba(232, 232, 232, 0.5);}#my-svg .cluster rect{fill:#ffffde;stroke:#aaaa33;stroke-width:1px;}#my-svg .cluster text{fill:#333;}#my-svg .cluster span{color:#333;}#my-svg div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:12px;background:hsl(80, 100%, 96.2745098039%);border:1px solid #aaaa33;border-radius:2px;pointer-events:none;z-index:100;}#my-svg .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#333;}#my-svg rect.text{fill:none;stroke-width:0;}#my-svg .icon-shape,#my-svg .image-shape{background-color:rgba(232,232,232, 0.8);text-align:center;}#my-svg .icon-shape p,#my-svg .image-shape p{background-color:rgba(232,232,232, 0.8);padding:2px;}#my-svg .icon-shape rect,#my-svg .image-shape rect{opacity:0.5;background-color:rgba(232,232,232, 0.8);fill:rgba(232,232,232, 0.8);}#my-svg :root{--mermaid-font-family:"trebuchet ms",verdana,arial,sans-serif;}</style><g><marker orient="auto" markerHeight="8" markerWidth="8" markerUnits="userSpaceOnUse" refY="5" refX="5" viewBox="0 0 10 10" class="marker flowchart-v2" id="my-svg_flowchart-v2-pointEnd"><path style="stroke-width: 1; stroke-dasharray: 1, 0;" class="arrowMarkerPath" d="M 0 0 L 10 5 L 0 10 z"/></marker><marker orient="auto" markerHeight="8" markerWidth="8" markerUnits="userSpaceOnUse" refY="5" refX="4.5" viewBox="0 0 10 10" class="marker flowchart-v2" id="my-svg_flowchart-v2-pointStart"><path style="stroke-width: 1; stroke-dasharray: 1, 0;" class="arrowMarkerPath" d="M 0 5 L 10 10 L 10 0 z"/></marker><marker orient="auto" markerHeight="11" markerWidth="11" markerUnits="userSpaceOnUse" refY="5" refX="11" viewBox="0 0 10 10" class="marker flowchart-v2" id="my-svg_flowchart-v2-circleEnd"><circle style="stroke-width: 1; stroke-dasharray: 1, 0;" class="arrowMarkerPath" r="5" cy="5" cx="5"/></marker><marker orient="auto" markerHeight="11" markerWidth="11" markerUnits="userSpaceOnUse" refY="5" refX="-1" viewBox="0 0 10 10" class="marker flowchart-v2" id="my-svg_flowchart-v2-circleStart"><circle style="stroke-width: 1; stroke-dasharray: 1, 0;" class="arrowMarkerPath" r="5" cy="5" cx="5"/></marker><marker orient="auto" markerHeight="11" markerWidth="11" markerUnits="userSpaceOnUse" refY="5.2" refX="12" viewBox="0 0 11 11" class="marker cross flowchart-v2" id="my-svg_flowchart-v2-crossEnd"><path style="stroke-width: 2; stroke-dasharray: 1, 0;" class="arrowMarkerPath" d="M 1,1 l 9,9 M 10,1 l -9,9"/></marker><marker orient="auto" markerHeight="11" markerWidth="11" markerUnits="userSpaceOnUse" refY="5.2" refX="-1" viewBox="0 0 11 11" class="marker cross flowchart-v2" id="my-svg_flowchart-v2-crossStart"><path style="stroke-width: 2; stroke-dasharray: 1, 0;" class="arrowMarkerPath" d="M 1,1 l 9,9 M 10,1 l -9,9"/></marker><g class="root"><g class="clusters"/><g class="edgePaths"><path marker-end="url(#my-svg_flowchart-v2-pointEnd)" style="" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" id="L_id0_id1_0" d="M548.426,41.384L472.482,48.987C396.539,56.59,244.652,71.795,168.709,82.897C92.766,94,92.766,101,92.766,104.5L92.766,108"/><path marker-end="url(#my-svg_flowchart-v2-pointEnd)" style="" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" id="L_id0_id2_1" d="M548.426,45.857L508.146,52.714C467.867,59.571,387.309,73.286,347.029,83.643C306.75,94,306.75,101,306.75,104.5L306.75,108"/><path marker-end="url(#my-svg_flowchart-v2-pointEnd)" style="" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" id="L_id0_id3_2" d="M561.418,62L553.581,66.167C545.745,70.333,530.072,78.667,522.235,86.333C514.398,94,514.398,101,514.398,104.5L514.398,108"/><path marker-end="url(#my-svg_flowchart-v2-pointEnd)" style="" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" id="L_id0_id4_3" d="M662.98,62L670.817,66.167C678.654,70.333,694.327,78.667,702.163,86.333C710,94,710,101,710,104.5L710,108"/><path marker-end="url(#my-svg_flowchart-v2-pointEnd)" style="" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" id="L_id0_id5_4" d="M675.973,46.345L714.061,53.121C752.148,59.897,828.324,73.448,866.412,83.724C904.5,94,904.5,101,904.5,104.5L904.5,108"/><path marker-end="url(#my-svg_flowchart-v2-pointEnd)" style="" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" id="L_id0_id6_5" d="M675.973,42.082L743.39,49.568C810.807,57.054,945.642,72.027,1013.059,83.014C1080.477,94,1080.477,101,1080.477,104.5L1080.477,108"/></g><g class="edgeLabels"><g class="edgeLabel"><g transform="translate(0, 0)" class="label"><foreignObject height="0" width="0"><div style="display: table-cell; white-space: nowrap; line-height: 1.5; max-width: 200px; text-align: center;" class="labelBkg" xmlns="http://www.w3.org/1999/xhtml"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g transform="translate(0, 0)" class="label"><foreignObject height="0" width="0"><div style="display: table-cell; white-space: nowrap; line-height: 1.5; max-width: 200px; text-align: center;" class="labelBkg" xmlns="http://www.w3.org/1999/xhtml"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g transform="translate(0, 0)" class="label"><foreignObject height="0" width="0"><div style="display: table-cell; white-space: nowrap; line-height: 1.5; max-width: 200px; text-align: center;" class="labelBkg" xmlns="http://www.w3.org/1999/xhtml"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g transform="translate(0, 0)" class="label"><foreignObject height="0" width="0"><div style="display: table-cell; white-space: nowrap; line-height: 1.5; max-width: 200px; text-align: center;" class="labelBkg" xmlns="http://www.w3.org/1999/xhtml"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g transform="translate(0, 0)" class="label"><foreignObject height="0" width="0"><div style="display: table-cell; white-space: nowrap; line-height: 1.5; max-width: 200px; text-align: center;" class="labelBkg" xmlns="http://www.w3.org/1999/xhtml"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g transform="translate(0, 0)" class="label"><foreignObject height="0" width="0"><div style="display: table-cell; white-space: nowrap; line-height: 1.5; max-width: 200px; text-align: center;" class="labelBkg" xmlns="http://www.w3.org/1999/xhtml"><span class="edgeLabel"></span></div></foreignObject></g></g></g><g class="nodes"><g transform="translate(612.19921875, 35)" id="flowchart-id0-0" class="node default"><rect height="54" width="127.546875" y="-27" x="-63.7734375" style="" class="basic label-container"/><g transform="translate(-33.7734375, -12)" style="" class="label"><rect/><foreignObject height="24" width="67.546875"><div style="display: table-cell; white-space: nowrap; line-height: 1.5; max-width: 200px; text-align: center;" xmlns="http://www.w3.org/1999/xhtml"><span class="nodeLabel"><p>obsession</p></span></div></foreignObject></g></g><g transform="translate(92.765625, 139)" id="flowchart-id1-1" class="node default"><rect height="54" width="169.53125" y="-27" x="-84.765625" style="" class="basic label-container"/><g transform="translate(-54.765625, -12)" style="" class="label"><rect/><foreignObject height="24" width="109.53125"><div style="display: table-cell; white-space: nowrap; line-height: 1.5; max-width: 200px; text-align: center;" xmlns="http://www.w3.org/1999/xhtml"><span class="nodeLabel"><p>debhelper(&gt;=9)</p></span></div></foreignObject></g></g><g transform="translate(306.75, 139)" id="flowchart-id2-3" class="node default"><rect height="54" width="158.4375" y="-27" x="-79.21875" style="" class="basic label-container"/><g transform="translate(-49.21875, -12)" style="" class="label"><rect/><foreignObject height="24" width="98.4375"><div style="display: table-cell; white-space: nowrap; line-height: 1.5; max-width: 200px; text-align: center;" xmlns="http://www.w3.org/1999/xhtml"><span class="nodeLabel"><p>libglib2.0-dev</p></span></div></foreignObject></g></g><g transform="translate(514.3984375, 139)" id="flowchart-id3-5" class="node default"><rect height="54" width="156.859375" y="-27" x="-78.4296875" style="" class="basic label-container"/><g transform="translate(-48.4296875, -12)" style="" class="label"><rect/><foreignObject height="24" width="96.859375"><div style="display: table-cell; white-space: nowrap; line-height: 1.5; max-width: 200px; text-align: center;" xmlns="http://www.w3.org/1999/xhtml"><span class="nodeLabel"><p>libdbus-1-dev</p></span></div></foreignObject></g></g><g transform="translate(710, 139)" id="flowchart-id4-7" class="node default"><rect height="54" width="134.34375" y="-27" x="-67.171875" style="" class="basic label-container"/><g transform="translate(-37.171875, -12)" style="" class="label"><rect/><foreignObject height="24" width="74.34375"><div style="display: table-cell; white-space: nowrap; line-height: 1.5; max-width: 200px; text-align: center;" xmlns="http://www.w3.org/1999/xhtml"><span class="nodeLabel"><p>libx11-dev</p></span></div></foreignObject></g></g><g transform="translate(904.5, 139)" id="flowchart-id5-9" class="node default"><rect height="54" width="154.65625" y="-27" x="-77.328125" style="" class="basic label-container"/><g transform="translate(-47.328125, -12)" style="" class="label"><rect/><foreignObject height="24" width="94.65625"><div style="display: table-cell; white-space: nowrap; line-height: 1.5; max-width: 200px; text-align: center;" xmlns="http://www.w3.org/1999/xhtml"><span class="nodeLabel"><p>libgtk2.0-dev</p></span></div></foreignObject></g></g><g transform="translate(1080.4765625, 139)" id="flowchart-id6-11" class="node default"><rect height="54" width="97.296875" y="-27" x="-48.6484375" style="" class="basic label-container"/><g transform="translate(-18.6484375, -12)" style="" class="label"><rect/><foreignObject height="24" width="37.296875"><div style="display: table-cell; white-space: nowrap; line-height: 1.5; max-width: 200px; text-align: center;" xmlns="http://www.w3.org/1999/xhtml"><span class="nodeLabel"><p>valac</p></span></div></foreignObject></g></g></g></g></g></svg>
```
3.Тесты:
![image](https://github.com/user-attachments/assets/9a3f69ce-5606-4920-9efc-450eba4126b3)

