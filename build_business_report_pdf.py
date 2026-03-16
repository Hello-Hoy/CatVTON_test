from __future__ import annotations

from pathlib import Path
from typing import List

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    Image,
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parent
SOURCE_MD = ROOT / "CATVTON_BUSINESS_REPORT_KO.md"
OUTPUT_DIR = ROOT / "output" / "pdf"
OUTPUT_PDF = OUTPUT_DIR / "catvton_business_report_ko_2026-03-16.pdf"
SAMPLE_IMAGE = ROOT / "outputs" / "full-resume" / "validation" / "post-train-unpaired-preview.png"
FONT_PATH = Path("/System/Library/Fonts/Supplemental/AppleGothic.ttf")
FONT_NAME = "AppleGothic"


def register_font() -> None:
    pdfmetrics.registerFont(TTFont(FONT_NAME, str(FONT_PATH)))


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="KoTitle",
            fontName=FONT_NAME,
            fontSize=24,
            leading=30,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#183153"),
            spaceAfter=10,
        )
    )
    styles.add(
        ParagraphStyle(
            name="KoSubtitle",
            fontName=FONT_NAME,
            fontSize=11,
            leading=16,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#4b5563"),
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="KoBody",
            parent=styles["BodyText"],
            fontName=FONT_NAME,
            fontSize=9.5,
            leading=15,
            wordWrap="CJK",
            spaceAfter=6,
            textColor=colors.HexColor("#111827"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="KoH1",
            parent=styles["Heading1"],
            fontName=FONT_NAME,
            fontSize=18,
            leading=24,
            textColor=colors.HexColor("#0f172a"),
            spaceBefore=10,
            spaceAfter=8,
            wordWrap="CJK",
        )
    )
    styles.add(
        ParagraphStyle(
            name="KoH2",
            parent=styles["Heading2"],
            fontName=FONT_NAME,
            fontSize=13,
            leading=18,
            textColor=colors.HexColor("#1d4ed8"),
            spaceBefore=8,
            spaceAfter=6,
            wordWrap="CJK",
        )
    )
    styles.add(
        ParagraphStyle(
            name="KoH3",
            parent=styles["Heading3"],
            fontName=FONT_NAME,
            fontSize=11,
            leading=15,
            textColor=colors.HexColor("#1f2937"),
            spaceBefore=6,
            spaceAfter=4,
            wordWrap="CJK",
        )
    )
    styles.add(
        ParagraphStyle(
            name="KoSmall",
            parent=styles["BodyText"],
            fontName=FONT_NAME,
            fontSize=8,
            leading=12,
            textColor=colors.HexColor("#6b7280"),
            wordWrap="CJK",
        )
    )
    return styles


def bullet_list(lines: List[str], styles) -> ListFlowable:
    items = []
    for line in lines:
        text = line[2:]
        items.append(ListItem(Paragraph(text, styles["KoBody"])))
    return ListFlowable(
        items,
        bulletType="bullet",
        bulletFontName=FONT_NAME,
        bulletFontSize=9,
        leftIndent=14,
    )


def parse_markdown(styles):
    story = []
    lines = SOURCE_MD.read_text(encoding="utf-8").splitlines()

    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        stripped = line.strip()
        if not stripped:
            i += 1
            continue

        if stripped.startswith("# "):
            story.append(Paragraph(stripped[2:], styles["KoH1"]))
            i += 1
            continue
        if stripped.startswith("## "):
            story.append(Paragraph(stripped[3:], styles["KoH2"]))
            i += 1
            continue
        if stripped.startswith("### "):
            story.append(Paragraph(stripped[4:], styles["KoH3"]))
            i += 1
            continue

        if stripped.startswith("- "):
            group = []
            while i < len(lines) and lines[i].strip().startswith("- "):
                group.append(lines[i].strip())
                i += 1
            story.append(bullet_list(group, styles))
            story.append(Spacer(1, 2 * mm))
            continue

        para = [stripped]
        i += 1
        while i < len(lines):
            current = lines[i].strip()
            if not current:
                break
            if current.startswith(("#", "-", "###")):
                break
            para.append(current)
            i += 1
        story.append(Paragraph(" ".join(para), styles["KoBody"]))
    return story


def cover_page(styles):
    story = []
    story.append(Spacer(1, 35 * mm))
    story.append(Paragraph("CatVTON 기반 비즈니스 모델 보고서", styles["KoTitle"]))
    story.append(Paragraph("Korea-first 패션 AI 사업화 검토안", styles["KoSubtitle"]))
    story.append(Paragraph("작성일: 2026-03-16", styles["KoSubtitle"]))
    story.append(Spacer(1, 12 * mm))

    summary = [
        ["핵심 추천안", "한국 여성 패션 브랜드와 에이전시 대상 온모델 이미지 생성 + 경량 try-on SaaS"],
        ["추천 판매 방식", "초기 6개월은 sales-led 파일럿, 이후 일부 self-serve 전환"],
        ["초기 가치 제안", "촬영 보완, 상세페이지 제작 속도 향상, 모델 다양성 확보"],
        ["가장 큰 리스크", "정밀 fit 보장을 과대약속하거나 운영 복잡도가 높아지는 것"],
    ]
    table = Table(summary, colWidths=[34 * mm, 130 * mm])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#e0f2fe")),
                ("BACKGROUND", (1, 0), (1, -1), colors.whitesmoke),
                ("FONTNAME", (0, 0), (-1, -1), FONT_NAME),
                ("FONTSIZE", (0, 0), (-1, -1), 10),
                ("LEADING", (0, 0), (-1, -1), 14),
                ("TEXTCOLOR", (0, 0), (-1, -1), colors.HexColor("#111827")),
                ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#93c5fd")),
                ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#bfdbfe")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ]
        )
    )
    story.append(table)
    story.append(Spacer(1, 10 * mm))
    story.append(
        Paragraph(
            "본 보고서는 현재 로컬 CatVTON 학습 자산과 최신 공개 자료를 결합해, 가장 실현 가능성이 높은 사업모델을 고르는 데 목적이 있다.",
            styles["KoBody"],
        )
    )
    story.append(PageBreak())
    return story


def decision_page(styles):
    story = [Paragraph("사업모델 선택 비교", styles["KoH1"])]
    data = [
        ["옵션", "기술 적합성", "지불 의사", "GTM 난이도", "판단"],
        ["소비자 앱", "중간", "불명확", "높음", "비추천"],
        ["브랜드 SaaS", "높음", "높음", "중간", "1순위"],
        ["에이전시 도구", "높음", "중간", "중간", "2순위"],
        ["플랫폼/API", "중간", "높음", "높음", "중장기"],
    ]
    table = Table(data, colWidths=[28 * mm, 28 * mm, 28 * mm, 30 * mm, 28 * mm])
    table.setStyle(
        TableStyle(
            [
                ("FONTNAME", (0, 0), (-1, -1), FONT_NAME),
                ("FONTSIZE", (0, 0), (-1, -1), 9),
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#183153")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("BACKGROUND", (0, 2), (-1, 2), colors.HexColor("#dcfce7")),
                ("BACKGROUND", (0, 3), (-1, 3), colors.HexColor("#ecfccb")),
                ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#94a3b8")),
                ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#cbd5e1")),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("ALIGN", (1, 1), (-1, -1), "CENTER"),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )
    story.append(table)
    story.append(Spacer(1, 8 * mm))
    story.append(
        Paragraph(
            "핵심 판단은 단순하다. 현재 CatVTON 자산은 소비자-facing 정밀 fit 엔진보다, 브랜드 실무용 온모델 이미지 생성과 경량 try-on 도구에 더 잘 맞는다.",
            styles["KoBody"],
        )
    )
    story.append(Spacer(1, 6 * mm))
    story.append(Paragraph("로컬 CatVTON 샘플 결과", styles["KoH2"]))
    if SAMPLE_IMAGE.exists():
        img = Image(str(SAMPLE_IMAGE))
        max_width = 155 * mm
        max_height = 135 * mm
        scale = min(max_width / img.imageWidth, max_height / img.imageHeight)
        img.drawWidth = img.imageWidth * scale
        img.drawHeight = img.imageHeight * scale
        story.append(img)
        story.append(
            Paragraph(
                "로컬 검증 산출물 예시. 이 문서에서는 이를 '정밀 피팅'이 아니라 '실무용 시각 자산 생성'의 증거로 해석한다.",
                styles["KoSmall"],
            )
        )
    story.append(PageBreak())
    return story


def add_page_number(canvas, doc):
    canvas.saveState()
    canvas.setFont(FONT_NAME, 8)
    canvas.setFillColor(colors.HexColor("#6b7280"))
    canvas.drawRightString(doc.pagesize[0] - 18 * mm, 10 * mm, f"{doc.page}")
    canvas.restoreState()


def main():
    register_font()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    styles = build_styles()
    doc = SimpleDocTemplate(
        str(OUTPUT_PDF),
        pagesize=A4,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=16 * mm,
        bottomMargin=16 * mm,
        title="CatVTON 기반 비즈니스 모델 보고서",
        author="Codex",
    )

    story = []
    story.extend(cover_page(styles))
    story.extend(decision_page(styles))
    story.extend(parse_markdown(styles))
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print(OUTPUT_PDF)


if __name__ == "__main__":
    main()
