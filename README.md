# Rozpoznávání ovoce a zeleniny na obrázcích
Autoři: Quan Nguyen, Šimon Šťastný

## Přehled

Tento projekt se zaměřuje na vytvoření modelu pro klasifikaci obrázků ovoce a zeleniny. Projekt využívá datovou sadu s obrázky 36 různých druhů ovoce a zeleniny. Cílem je vytvořit model, který dokáže tyto obrázky přesně klasifikovat.

## Co projekt dělá

Tento projekt vyvíjí a trénuje model strojového učení, který je schopen identifikovat 36 různých druhů ovoce a zeleniny z obrázků. Využívá techniky hlubokého učení, konkrétně konvoluční neuronové sítě (CNN), k extrakci rysů z obrázků a k přesným předpovědím.

## Proč je projekt užitečný

Tento projekt pro nás sloužil k vyskoušení hlubokévo učení na klasifikaci obrázků (multiclass single-label). Jeho rozšíření však může najít uplatnění v několika praktických oblastech:

- **Automatické pokladny v obchodech s potravinami:** Model lze integrovat do samoobslužných pokladen, aby automaticky identifikoval ovoce a zeleninu a urychlil tak proces placení.
- **Správa zásob:** Obchodníci mohou model využít ke sledování úrovně zásob ovoce a zeleniny automatickou analýzou obrázků regálů.
- **Sledování stravy:** Model lze začlenit do aplikací, které pomáhají uživatelům sledovat jejich příjem potravy a nutriční informace.

## Jak spustit projekt u sebe

1. **Naklonujte úložiště:** `git clone https://github.com/smnststn/Fruits_vegetables.git`
2. **Nainstalujte závislosti:** `pip install -r requirements.txt`
3. **Stáhněte si datovou sadu:** Upravte cestu k načítání dat v kódu tak, aby směřovala na umístění datové sady obsahující obrázky ovoce a zeleniny. Pokud chcete rozšířit trénovací dataset, načtěte soubor `train_addition.zip` a nastavte parametr `additional = True`.
4. **Spusťte kód:** Spusťte Jupyter Notebook nebo Python skripty pro trénování a vyhodnocení modelu.

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
        - Vlastní model CNN.
        - Transfer learning s MobileNetV3 large & VGG16
    - Knihovna Keras byla použita pro vytvoření a trénování modelu.

3. **Trénování a vyhodnocení modelu:**
    - Modely byly trénovány na trénovacích datech a vyhodnoceny na validačních datech.
    - K posouzení výkonu modelu byly použity metriky výkonu, jako je přesnost, ztráta, precision, recall a F1-skóre.
    - Byly generovány matice záměn a klasifikační reporty pro identifikaci specifických oblastí, kde model fungoval dobře, a oblastí, které je třeba zlepšit.

## Závěr

- Projekt demonstroval úspěšné použití konvolučních neuronových sítí pro klasifikaci obrazu.
- Vlastní model i transfer learning s MobileNetV3 large & VGG16 dosáhly rozumné přesnosti v klasifikaci obrázků ovoce a zeleniny.
- Specifické výzvy a oblasti pro zlepšení byly identifikovány prostřednictvím matic záměn a klasifikačních reportů.
- Jemné doladění architektury modelu, prozkoumání dalších technik augmentace dat a testování s většími a rozmanitějšími datovými sadami může dále zlepšit přesnost a generalizaci modelu.
- Nejlepší model naleznete v ve větve `nejlepsi_model` (https://github.com/smnststn/Fruits_vegetables/tree/nejlepsi_model).

## Možnosti další práce

- Jemné doladění hyperparametrů modelu pro další zlepšení jeho výkonu.
- Prozkoumání použití jiných architektur nebo optimalizačních algoritmů.
- Zvýšení velikosti a rozmanitosti datové sady pro zlepšení generalizačních schopností modelu.
- Vývoj webové aplikace, která využívá model pro klasifikaci ovoce a zeleniny v reálném čase.
