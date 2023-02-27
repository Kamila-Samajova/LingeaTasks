# Jak už píšete i v zadání, problém ohodnocení kvality strojového překladu
# není jednoznačný a přístupy k řešení mohou být různé. Já jsem při studování
# této problematiky narazila na 2 hlavní metriky, které mě zaujaly a přišly
# mi užitečné.
#
# Prvním z nich je metrika BLEU, která porovnává strojový překlad s lidským
# a poskytuje skóre na základě shody mezi těmito překlady - čím vyšší skóre
# tím lepší překlad. BLEU může být implementováno pomocí různých knihoven
# pro zpracování přirozeného jazyka. Níže uvádím kousek kódu využívající
# BLEU skóre.
#
# Druhou metrikou je WER (Word Error Rate), což je metrika, která porovnává
# počet chyb v jednotlivých slovech mezi strojovým a lidským překladem. Zde
# naopak čím nižší je výsledné skóre - chyba, tím výšší je kvalita překladu.
# Příklad kódu s využitím této metriky také uvádím níže.


# načtení lidských překladů z human.txt
with io.open('human.txt', 'r', encoding='utf-8') as f:
    human_sentences = [line.strip().split() for line in f]

# načtení strojových překladů z machine.txt
with io.open('machine.txt', 'r', encoding='utf-8') as f:
    machine_sentences = [line.strip().split() for line in f]


# výpočet BLEU skóre mezi strojovými překlady a lidskými překlady
bleu_score = corpus_bleu([[ref] for ref in human_sentences], machine_sentences)

# výpis výsledku
print(f"BLEU score: {bleu_score}")


# funkce pro výpočet WER mezi dvěma větami
def wer(h, m):
    n, m = len(h), len(m)
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = i
    for j in range(m+1):
        dp[0][j] = j
    for i in range(1, n+1):
        for j in range(1, m+1):
            if h[i-1] == m[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[n][m]


# výpočet WER skóre mezi strojovými překlady a lidskými překlady
total_wer = 0
for i in range(len(human_sentences)):
    total_wer += wer(human_sentences[i], machine_sentences[i])
wer_score = total_wer / len(human_sentences)

# výpis výsledku
print(f"WER score: {wer_score}")
