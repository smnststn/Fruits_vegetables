# Rozpoznávání ovoce a zeleniny na obrázcích

## Přehled

Tento projekt se zaměřuje na vytvoření modelu pro klasifikaci obrázků ovoce a zeleniny. Projekt využívá datovou sadu s obrázky 36 různých druhů ovoce a zeleniny. Cílem je vytvořit model, který dokáže tyto obrázky přesně klasifikovat.

## Co projekt dělá

Tento projekt vyvíjí a trénuje model strojového učení, který je schopen identifikovat 36 různých druhů ovoce a zeleniny z obrázků. Využívá techniky hlubokého učení, konkrétně konvoluční neuronové sítě (CNN), k extrakci rysů z obrázků a k přesným předpovědím.

## Proč je projekt užitečný

Tento projekt má několik praktických aplikací:

- **Automatické pokladny v obchodech s potravinami:** Model lze integrovat do samoobslužných pokladen, aby automaticky identifikoval ovoce a zeleninu a urychlil tak proces placení.
- **Správa zásob:** Obchodníci mohou model využít ke sledování úrovně zásob ovoce a zeleniny automatickou analýzou obrázků regálů.
- **Sledování stravy:** Model lze začlenit do aplikací, které pomáhají uživatelům sledovat jejich příjem potravy a nutriční informace.
- **Zemědělské aplikace:** Zemědělci mohou model využít k identifikaci chorob nebo škůdců na plodinách na základě analýzy obrazu.
- **Vzdělávací nástroj:** Projekt slouží jako vzdělávací nástroj pro učení o hlubokém učení a klasifikaci obrazu.

## Jak začít

1. **Naklonujte úložiště:** `git clone [URL úložiště]`
2. **Nainstalujte závislosti:** `pip install -r requirements.txt`
3. **Stáhněte si datovou sadu:** Nakonfigurujte cestu k načítání dat v kódu tak, aby ukazovala na umístění datové sady s obrázky ovoce a zeleniny.
4. **Spusťte kód:** Spusťte Jupyter Notebook nebo Python skripty pro trénování a vyhodnocení modelu.

## Získání nápovědy

Pokud narazíte na nějaké problémy nebo máte dotazy, podívejte se do dokumentace projektu nebo otevřete problém v úložišti GitHub. Komunita a správci vám rádi pomohou.

## Správci a přispěvatelé

Tento projekt spravuje [vaše jméno] a je otevřený příspěvkům od komunity. Pokud chcete přispět, neváhejte rozvětvit úložiště a odeslat žádost o pull request.


## Použité nástroje

- **Python:** Hlavní programovací jazyk použitý pro tento projekt.
- **Google Colab:** Cloudová platforma pro spouštění kódu Python, použitá pro trénování a analýzu modelu.
- **TensorFlow/Keras:** Knihovny hlubokého učení použité pro vytváření a trénování modelu.
- **PyTorch:** Framework hlubokého učení použitý pro generování heatmap.
- **OpenCV (cv2):** Knihovna pro úkoly počítačového vidění, použitá pro předzpracování obrazu.
- **NumPy:** Knihovna pro numerické výpočty.
- **Pandas:** Knihovna pro manipulaci a analýzu dat.
- **Scikit-learn:** Knihovna pro úkoly strojového učení, použitá pro vyhodnocení modelu.
- **Matplotlib:** Knihovna pro vytváření vizualizací.
- **PIL (Pillow):** Knihovna pro zpracování obrazu.
- **KaggleHub:** Používá se ke stahování a správě datových sad.

## Provedená analýza

1. **Načtení a předzpracování dat:**
    - Obrázky ovoce a zeleniny byly načteny z datové sady.
    - Obrázky byly změněny a normalizovány, aby byly připraveny pro model.
    - Štítky byly numericky zakódovány pro použití v modelu.

2. **Vytvoření modelu:**
    - Byly vytvořeny a porovnány dva modely:
        - Vlastní model CNN inspirovaný VGG16.
        - Transfer learning s MobileNetV3 large.
    - Knihovna Keras byla použita pro vytvoření a trénování modelu.

3. **Trénování a vyhodnocení modelu:**
    - Modely byly trénovány na trénovacích datech a vyhodnoceny na validačních datech.
    - K posouzení výkonu modelu byly použity metriky výkonu, jako je přesnost, ztráta, precision, recall a F1-skóre.
    - Byly generovány matice záměn a klasifikační reporty pro identifikaci specifických oblastí, kde model fungoval dobře, a oblastí, které je třeba zlepšit.

4. **Generování heatmap:**
    - VGG16 byl použit k generování aktivačních heatmap pro nesprávné předpovědi. 
    - Tato vizualizační technika pomáhá identifikovat oblasti obrazu, na které se model zaměřuje při klasifikaci, zlepšuje interpretovatelnost modelu a identifikuje potenciální oblasti pro zlepšení.

## Poznatky

- Projekt demonstroval úspěšné použití konvolučních neuronových sítí pro klasifikaci obrazu.
- Vlastní model i transfer learning s MobileNetV3 dosáhly rozumné přesnosti v klasifikaci obrázků ovoce a zeleniny.
- Specifické výzvy a oblasti pro zlepšení byly identifikovány prostřednictvím matic záměn a klasifikačních reportů.
- Jemné doladění architektury modelu, prozkoumání dalších technik augmentace dat a testování s většími a rozmanitějšími datovými sadami může dále zlepšit přesnost a generalizaci modelu.
- Heatmapy poskytly vhled do procesu rozhodování modelu a odhalily, které oblasti obrazu ovlivňují výsledky klasifikace.

## Budoucí práce

- Jemné doladění hyperparametrů modelu pro další zlepšení jeho výkonu.
- Prozkoumání použití jiných architektur nebo optimalizačních algoritmů.
- Zvýšení velikosti a rozmanitosti datové sady pro zlepšení generalizačních schopností modelu.
- Vývoj webové aplikace, která využívá model pro klasifikaci ovoce a zeleniny v reálném čase.
