# [Gold V] Marked-Numbered - 28270 

[문제 링크](https://www.acmicpc.net/problem/28270) 

### 성능 요약

메모리: 161416 KB, 시간: 708 ms

### 분류

자료 구조, 스택, 트리

### 제출 일자

2024년 10월 12일 13:14:23

### 문제 설명

<p>코치 희승이는 FXC 나라 육상 국가대표 선발 보고서를 작성하였다. 희승이는 보고서를 작성할 때 목차를 육상협회에서 사용하는 글머리 <strong>기호</strong> 형태로 작성하였다. 희승이가 FXC 나라 문화체육관광부로 공문을 보내려고 봤더니, 문화체육관광부에서는 공문을 작성할 때 글머리 <strong>번호</strong> 형태로 작성한다. 따라서 희승이는 보고서를 글머리 <strong>번호</strong> 형태로 바꾼 사본을 만들어서 문화체육관광부로 보내려고 한다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/616b710a-fdc0-4bce-bd7d-13d77aa4e1d9/-/preview/" style="width: 1006px; height: 300px;"></p>

<p>보고서 목차는 위 그림의 트리와 같이 도식화할 수 있다. 트리에서 루트를 제외한 모든 노드는 보고서의 항목과 일대일 대응된다. 트리에서 깊이 우선 탐색(DFS)을 했을 때 방문하는 순서대로 트리 노드에 색인을 매길 수 있는데, 보고서에서 먼저 등장하는 항목이 더 작은 색인을 가진다. 보고서를 글머리 <strong>기호</strong> 형태로 작성한다면 각 항목의 번호는 항목과 대응하는 노드의 레벨(루트 노드와의 거리)과 같다. 한편 보고서를 글머리 <strong>번호</strong> 형태로 작성한다면 각 항목의 번호는 항목과 대응하는 노드보다 색인이 작은 형제 노드의 수에 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container>을 더한 값과 같다.</p>

<p>희승이가 글머리 <strong>기호</strong> 형태로 작성한 보고서 목차가 주어지면 이를 글머리 <strong>번호</strong> 형태로 변환하는 프로그램을 작성하여라.</p>

### 입력 

 <p>첫 번째 줄에 보고서 목차 내 항목의 개수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D436 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$C$</span></mjx-container>가 주어진다.</p>

<p>두 번째 줄에는 글머리 <strong>기호</strong> 형태로 작성된 보고서에서 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2B"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>+</mo><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$i+1$</span></mjx-container>번째(<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D436 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>≤</mo><mi>i</mi><mo><</mo><mi>C</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0 \leq i < C$</span></mjx-container>) 항목의 번호 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.081em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>M</mi><mi>i</mi></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M_i$</span></mjx-container>에 해당하는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D436 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$C$</span></mjx-container>개의 정수가 주어진다.</p>

### 출력 

 <p>만약 주어진 보고서가 올바른 보고서가 아닌 경우 첫 번째 줄에 <code>-1</code>을 출력한다. 보고서가 올바르다면 항목의 번호가 입력과 동일하게 매겨지도록 보고서와 대응되는 트리를 만들 수 있다.</p>

<p>주어진 보고서가 올바른 보고서라면 첫 번째 줄에 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D436 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$C$</span></mjx-container>개의 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.085em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>N</mi><mi>i</mi></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N_i$</span></mjx-container>를 출력한다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.085em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>N</mi><mi>i</mi></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N_i$</span></mjx-container>는 주어진 보고서를 글머리 <strong>번호</strong> 형태로 바꿨을 때 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2B"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>+</mo><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$i+1$</span></mjx-container>번째(<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D436 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>≤</mo><mi>i</mi><mo><</mo><mi>C</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0 \leq i < C$</span></mjx-container>) 항목의 번호를 의미한다.</p>

<p>가능한 정답이 여러 가지라면 그중 아무거나 출력한다.</p>

