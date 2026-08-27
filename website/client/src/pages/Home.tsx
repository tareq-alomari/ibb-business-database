/**
 * Style contract — خريطة المعرفة الحيّة:
 * واجهة تحريرية مدنية بألوان ورقية دافئة وخط مسار طبوغرافي؛ كل قسم يشرح انتقال المشروع
 * من البيانات المتفرقة إلى قرار قابل للتنفيذ، مع تجنب البطاقات التسويقية المتكررة.
 */
import { useEffect, useState } from "react";
import {
  ArrowDownLeft,
  ArrowLeft,
  ArrowUpLeft,
  BarChart3,
  BookOpenCheck,
  ChevronDown,
  ClipboardCheck,
  Database,
  ExternalLink,
  FileText,
  Layers3,
  MapPinned,
  Menu,
  Network,
  ShieldCheck,
  Sparkles,
  X,
} from "lucide-react";

const navigation = [
  { label: "الفكرة", href: "#idea" },
  { label: "نطاق التغطية", href: "#coverage" },
  { label: "منهجية العمل", href: "#method" },
  { label: "خارطة التنفيذ", href: "#roadmap" },
  { label: "الحقوق والتواصل", href: "#connect" },
];

const sectors = [
  "الصحة",
  "التعليم",
  "التجارة والتجزئة",
  "الأغذية والمشروبات",
  "التقنية والاتصالات",
  "المال والأعمال",
  "العقارات والإنشاءات",
  "النقل والمواصلات",
  "السيارات",
  "الزراعة والثروة الحيوانية",
  "الصناعة والإنتاج",
  "الخدمات المهنية",
  "الخدمات المنزلية",
  "التجميل والعناية",
  "السياحة والضيافة",
  "المنظمات والجمعيات",
  "الجهات الحكومية",
  "الإعلام والإعلان",
  "الرياضة والترفيه",
  "الطاقة والمرافق",
  "الأسواق الشعبية",
  "الحرف التقليدية",
];

const phases = [
  "اكتشاف المشروع",
  "البحث",
  "تحليل الأعمال",
  "تحليل السوق",
  "تحليل المنافسين",
  "أصحاب المصلحة",
  "بحث المستخدم",
  "التحليل الوظيفي",
  "المتطلبات غير الوظيفية",
  "هيكل المعلومات",
  "تجربة المستخدم",
  "تصميم الواجهة",
  "تصميم قاعدة البيانات",
  "تصميم API",
  "هندسة البرمجيات",
  "المكدس التقني",
  "الأمان",
  "تحسين الظهور",
  "لوحة التحكم",
  "تخطيط المشروع",
  "التوثيق",
  "التسليمات النهائية",
];

const foundationItems = [
  {
    number: "01",
    title: "بيانات منظمة",
    copy: "147 مجالًا تحليليًا يجمعها قاموس واحد: الخدمات والشرائح والفرص والمتطلبات.",
    icon: Database,
  },
  {
    number: "02",
    title: "تحليل قابل للتتبع",
    copy: "22 محطة عمل تربط البحث بالسوق والمنتج والتقنية وخطة التشغيل.",
    icon: Layers3,
  },
  {
    number: "03",
    title: "بناء مسؤول",
    copy: "تفرقة واضحة بين ما هو موثق، وما هو تقديري، وما يحتاج تحققًا ميدانيًا.",
    icon: ShieldCheck,
  },
];

const roadmap = [
  {
    number: "01",
    title: "تنظيف الهيكل",
    text: "توحيد المجلدات وأسماء المراحل وإزالة التكرار في بنية المستودع.",
    tag: "تهيئة الأساس",
  },
  {
    number: "02",
    title: "تثبيت مسار البيانات",
    text: "تحويل مولدات الملفات إلى مسارات نسبية مع إعداد تشغيل واختبارات واضحة.",
    tag: "قابلية الإعادة",
  },
  {
    number: "03",
    title: "بناء سجل حقيقي",
    text: "إنشاء نموذج بيانات منظم للمنشآت والمواقع والفئات وحالة التحقق.",
    tag: "بيانات تشغيلية",
  },
  {
    number: "04",
    title: "توثيق الثقة",
    text: "إسناد كل معلومة إلى رابط مصدر وتاريخ تحقق ومنهج جمع ودرجة موثوقية.",
    tag: "شفافية",
  },
  {
    number: "05",
    title: "إطلاق MVP واحد",
    text: "اختيار قطاع المستشفيات نقطة بداية عملية للبحث والخريطة والتحديث الميداني.",
    tag: "منتج أولي",
  },
  {
    number: "06",
    title: "التوسع المدروس",
    text: "إضافة الواجهة وAPI ولوحة الإدارة، ثم تعميم النموذج على القطاعات تدريجيًا.",
    tag: "نمو مستدام",
  },
];

function SectionKicker({ children }: { children: string }) {
  return (
    <p className="section-kicker">
      <span aria-hidden="true" />
      {children}
    </p>
  );
}

export default function Home() {
  const [menuOpen, setMenuOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 24);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  const closeMenu = () => setMenuOpen(false);

  return (
    <div className="min-h-screen overflow-x-hidden bg-[#f8f3e9] text-[#15302d]" dir="rtl">
      <header className={`site-header ${scrolled ? "site-header--scrolled" : ""}`}>
        <div className="header-inner">
          <a href="#top" className="brand" aria-label="IBB Business Database - الصفحة الرئيسية">
            <img src="/manus-storage/ibb-mark_01c90183.png" alt="رمز منصة IBB" />
            <span className="brand-lockup">
              <strong><b>IBB</b><span>دليل المعرفة</span></strong>
              <small>قاعدة أعمال إب</small>
            </span>
          </a>

          <nav className="desktop-nav" aria-label="التنقل الرئيسي">
            {navigation.map((item) => (
              <a key={item.href} href={item.href}>
                {item.label}
              </a>
            ))}
          </nav>

          <a className="header-cta" href="#roadmap">
            ابدأ من الخريطة
            <ArrowLeft size={16} strokeWidth={2.2} />
          </a>

          <button
            className="menu-trigger"
            type="button"
            aria-label={menuOpen ? "إغلاق القائمة" : "فتح القائمة"}
            aria-expanded={menuOpen}
            onClick={() => setMenuOpen((current) => !current)}
          >
            {menuOpen ? <X size={22} /> : <Menu size={22} />}
          </button>
        </div>

        {menuOpen && (
          <nav className="mobile-nav" aria-label="التنقل على الهاتف">
            {navigation.map((item) => (
              <a key={item.href} href={item.href} onClick={closeMenu}>
                {item.label}
                <ArrowLeft size={17} />
              </a>
            ))}
            <a href="#roadmap" onClick={closeMenu} className="mobile-nav-action">
              ابدأ من الخريطة
            </a>
          </nav>
        )}
      </header>

      <main id="top">
        <div className="atlas-spine" aria-hidden="true">
          <span className="atlas-spine__label">مسار الأطلس</span>
          <i className="atlas-spine__node atlas-spine__node--one" />
          <i className="atlas-spine__node atlas-spine__node--two" />
          <i className="atlas-spine__node atlas-spine__node--three" />
          <i className="atlas-spine__node atlas-spine__node--four" />
        </div>
        <section className="hero" aria-labelledby="hero-heading">
          <div className="hero-map" aria-hidden="true" />
          <div className="hero-grid" aria-hidden="true" />
          <div className="hero-content">
            <div className="hero-statement reveal">
              <div className="hero-eyebrow">
                <MapPinned size={17} />
                <span>محافظة إب · اليمن</span>
                <i />
                <span>منصة معرفة محلية</span>
              </div>
              <h1 id="hero-heading">
                من المعلومة المتفرقة
                <em> إلى خريطة قرار واحدة.</em>
              </h1>
              <p>
                مشروع يوثق مشهد الأعمال والخدمات في محافظة إب، ثم يحوّل فهمه إلى بنية قابلة للبحث والتحليل والبناء المسؤول.
              </p>
              <div className="hero-actions">
                <a className="btn-primary" href="#idea">
                  اقرأ الفكرة
                  <ArrowDownLeft size={18} />
                </a>
                <a className="btn-plain" href="#method">
                  تعرّف إلى المنهجية
                  <ArrowLeft size={17} />
                </a>
              </div>
            </div>

            <aside className="hero-compass reveal reveal-delay" aria-label="مؤشرات المشروع الرئيسية">
              <div className="compass-orbit compass-orbit--one" />
              <div className="compass-orbit compass-orbit--two" />
              <div className="compass-center">
                <span>منصة</span>
                <strong>معرفة</strong>
                <small>محلية</small>
              </div>
              <div className="compass-note compass-note--north">بيانات</div>
              <div className="compass-note compass-note--east">تحليل</div>
              <div className="compass-note compass-note--south">تطبيق</div>
            </aside>
          </div>
          <div className="hero-bottom-rule" aria-hidden="true">
            <span>مرّر لتتبع المسار</span>
            <ChevronDown size={18} />
          </div>
        </section>

        <section className="metrics-section" aria-label="مؤشرات نطاق المشروع">
          <div className="content-frame metrics-frame">
            <div className="metrics-intro">
              <span className="mini-mark" aria-hidden="true"><Layers3 size={19} /></span>
              <p>المستودع في أرقام</p>
            </div>
            <dl className="metrics-list">
              <div>
                <dt>147</dt>
                <dd>مجالًا تحليليًا</dd>
              </div>
              <div>
                <dt>22</dt>
                <dd>مرحلة منهجية</dd>
              </div>
              <div>
                <dt>3,259</dt>
                <dd>ملف Markdown متتبع</dd>
              </div>
              <div>
                <dt>10</dt>
                <dd>مولدات Python</dd>
              </div>
            </dl>
          </div>
        </section>

        <section id="idea" className="section idea-section" aria-labelledby="idea-heading">
          <div className="content-frame split-intro">
            <div className="intro-column">
              <SectionKicker>لماذا وُجدت المنصة؟</SectionKicker>
              <h2 id="idea-heading">المعرفة المحلية تستحق بنية لا مجرد ملفات.</h2>
            </div>
            <div className="body-column">
              <p className="lead-copy">
                يضع المشروع أساسًا لدليل أعمال وخدمات محلي: قاعدة تحليل واسعة للمؤسسات والمحلات والقطاعات، تُبنى لتخدم المواطن والباحث والمنظمة والجهة المعنية بالتخطيط.
              </p>
              <p>
                لا يدّعي الموقع أن كل ما فيه سجل رسمي مكتمل؛ بل يوضح بصدق ما هو متاح اليوم، وما ينبغي تحويله إلى بيانات موثقة وقابلة للتحديث قبل إطلاقه كخدمة عامة.
              </p>
              <a className="text-link" href="#truth">
                شاهد الصورة الكاملة للمشروع <ArrowLeft size={17} />
              </a>
            </div>
          </div>
        </section>

        <section id="coverage" className="coverage-section" aria-labelledby="coverage-heading">
          <div className="coverage-top content-frame">
            <div>
              <SectionKicker>نطاق التغطية</SectionKicker>
              <h2 id="coverage-heading">22 قطاعًا رئيسيًا، تنطلق منها قراءة اقتصادية واجتماعية واحدة.</h2>
            </div>
            <p>
              التقسيم لا يهدف إلى الحصر الشكلي؛ بل يهيئ لغة مشتركة بين البيانات الميدانية، وتحليل السوق، ومتطلبات المنتج الرقمي.
            </p>
          </div>
          <div className="sector-atlas content-frame">
            <aside className="sector-legend" aria-label="مفتاح فهرس القطاعات">
              <div className="legend-seal"><span>22</span><small>قطاعًا</small></div>
              <p>فهرس الأطلس</p>
              <small>كل رقم يمثل طبقة قابلة للتحليل والتوسع والتحقق.</small>
            </aside>
            <div className="sector-stream" role="list" aria-label="القطاعات الرئيسية">
              {sectors.map((sector, index) => (
                <div key={sector} className="sector-chip" role="listitem">
                  <span>{String(index + 1).padStart(2, "0")}</span>
                  <strong>{sector}</strong>
                </div>
              ))}
            </div>
          </div>
          <div className="coverage-foot content-frame">
            <p><span /> البيانات تبدأ بالتجميع، لكن قيمتها تظهر حين ترتبط بالسياق والناس والقرار.</p>
          </div>
        </section>

        <section id="method" className="section method-section" aria-labelledby="method-heading">
          <div className="path-line" aria-hidden="true"><span /></div>
          <div className="content-frame method-layout">
            <div className="method-visual">
              <div className="image-frame image-frame--layers">
                <img src="/manus-storage/ibb-data-layers_847a3348.jpg" alt="طبقات دائرية تجسد البيانات والتحليل والتطبيق" />
              </div>
              <p className="image-caption"><span>ثلاث طبقات</span> تتحول فيها المعلومة إلى نظام قابل للعمل.</p>
            </div>
            <div className="method-copy">
              <SectionKicker>بنية المعرفة</SectionKicker>
              <h2 id="method-heading">من ملف وصفي إلى مسار تطوير قابل للفهم.</h2>
              <p className="lead-copy">
                لا يُختزل كل قطاع في صفحة تعريفية. يمر عبر محطات محددة تجعل الأسئلة التجارية والإنسانية والتقنية مرئية قبل بناء أي منتج.
              </p>
              <div className="foundation-list">
                {foundationItems.map((item) => {
                  const Icon = item.icon;
                  return (
                    <article className="foundation-item" key={item.number}>
                      <div className="foundation-number">{item.number}</div>
                      <div className="foundation-icon"><Icon size={21} /></div>
                      <div>
                        <h3>{item.title}</h3>
                        <p>{item.copy}</p>
                      </div>
                    </article>
                  );
                })}
              </div>
            </div>
          </div>
        </section>

        <section className="stages-section" aria-labelledby="stages-heading">
          <div className="content-frame stages-heading-row">
            <div>
              <SectionKicker>منهجية التحليل</SectionKicker>
              <h2 id="stages-heading">22 محطة قبل أن تصبح الفكرة منتجًا.</h2>
            </div>
            <p>تُنظم المراحل رحلة التحليل بدءًا من اكتشاف المشكلة ووصولًا إلى التسليمات وخطة التنفيذ.</p>
          </div>
          <div className="stages-rail" aria-label="مراحل التحليل الاثنتان والعشرون">
            {phases.map((phase, index) => (
              <article className="stage" key={phase}>
                <span className="stage-number">{String(index + 1).padStart(2, "0")}</span>
                <div className="stage-dot" aria-hidden="true" />
                <h3>{phase}</h3>
              </article>
            ))}
          </div>
          <div className="content-frame stages-note">
            <BookOpenCheck size={21} />
            <p>كل محطة هي وثيقة عمل مستقلة، لا مجرد عنوان في عرض تقديمي.</p>
          </div>
        </section>

        <section id="truth" className="section truth-section" aria-labelledby="truth-heading">
          <div className="content-frame truth-layout">
            <div className="truth-copy">
              <SectionKicker>صورة صادقة عن الحاضر</SectionKicker>
              <h2 id="truth-heading">ما تم بناؤه اليوم: قاعدة تحليل واسعة، لا منصة تشغيلية مكتملة.</h2>
              <p className="lead-copy">
                القيمة الحالية في عمق التوثيق واتساع النطاق. أما الواجهة العامة، وقاعدة السجلات، وعمليات التحقق والتحديث، فما زالت خطوات تالية يجب بناؤها بعناية.
              </p>
              <div className="truth-grid">
                <article>
                  <FileText size={20} />
                  <h3>وثائق ومولدات</h3>
                  <p>آلاف ملفات التحليل مع سكربتات تنشئ البنية وتعبئ القوالب.</p>
                </article>
                <article>
                  <Network size={20} />
                  <h3>لا API أو واجهة بعد</h3>
                  <p>التصورات التقنية موجودة، أما التطبيق وقاعدة البيانات التشغيلية فليسا داخل المستودع.</p>
                </article>
                <article>
                  <ClipboardCheck size={20} />
                  <h3>التحقق أولوية</h3>
                  <p>الأرقام التقديرية تحتاج مصادر مباشرة وتاريخ تحقق قبل استخدامها كسجل عام.</p>
                </article>
              </div>
            </div>
            <div className="truth-side">
              <div className="archive-specimen" aria-label="تصور بصري لملف المعرفة المحلي">
                <span className="specimen-label specimen-label--top">ملف أطلس / 147</span>
                <div className="specimen-sheet specimen-sheet--back" />
                <div className="specimen-sheet specimen-sheet--middle" />
                <div className="specimen-sheet specimen-sheet--front">
                  <span className="specimen-label">مفتاح القراءة</span>
                  <div className="specimen-rings"><img src="/manus-storage/ibb-mark_01c90183.png" alt="" /></div>
                  <div className="specimen-lines"><i /><i /><i /><i /></div>
                  <p>بيانات<br />تحليل<br /><em>تحقق</em></p>
                </div>
                <span className="specimen-label specimen-label--side">إب · اليمن</span>
              </div>
              <div className="truth-stamp">
                <span>القرار التالي</span>
                <strong>تحويل التوثيق إلى<br />بيانات قابلة للتحديث.</strong>
                <ArrowUpLeft size={22} />
              </div>
            </div>
          </div>
        </section>

        <section className="hospital-section" aria-labelledby="hospital-heading">
          <div className="content-frame hospital-layout">
            <div className="hospital-flag">
              <span>نموذج مرجعي</span>
              <BarChart3 size={22} />
            </div>
            <div className="hospital-main">
              <SectionKicker>قطاع المستشفيات</SectionKicker>
              <h2 id="hospital-heading">المستشفيات: أعمق نموذج في المستودع، وبداية منطقية للـMVP.</h2>
              <p>
                يقدم هذا القطاع تصورًا لنظام معلومات رقمي: دليل مستشفيات، بحث وتصنيف، خريطة، مؤشرات، ووثائق للمتطلبات وقاعدة البيانات وواجهة API.
              </p>
              <a className="btn-dark" href="#roadmap">
                شاهد مسار التحويل إلى منتج
                <ArrowLeft size={18} />
              </a>
            </div>
            <dl className="hospital-stats">
              <div><dt>1,289</dt><dd>سطرًا في التقرير الموسع</dd></div>
              <div><dt>160+</dt><dd>مستشفى كهدف للحصر</dd></div>
              <div><dt>6</dt><dd>أشهر كخطة تطوير</dd></div>
            </dl>
          </div>
        </section>

        <section id="roadmap" className="section roadmap-section" aria-labelledby="roadmap-heading">
          <div className="content-frame roadmap-header">
            <div>
              <SectionKicker>خارطة التنفيذ</SectionKicker>
              <h2 id="roadmap-heading">من أرشيف موثق إلى خدمة عامة يمكن الوثوق بها.</h2>
            </div>
            <p>
              المسار المقترح يحافظ على قيمة العمل الموجود، لكنه يغيّر طبيعته تدريجيًا من ملفات تحليل إلى نظام بيانات ومنتج رقمي حي.
            </p>
          </div>
          <div className="content-frame roadmap-list">
            {roadmap.map((step, index) => (
              <article className={`roadmap-item ${index % 2 === 0 ? "roadmap-item--right" : "roadmap-item--left"}`} key={step.number}>
                <div className="roadmap-pin"><span>{step.number}</span></div>
                <div className="roadmap-card">
                  <p>{step.tag}</p>
                  <h3>{step.title}</h3>
                  <span>{step.text}</span>
                </div>
              </article>
            ))}
          </div>
        </section>

        <section id="connect" className="stewardship-section" aria-labelledby="connect-heading">
          <div className="content-frame stewardship-layout">
            <div className="stewardship-intro">
              <SectionKicker>الإسناد والتواصل</SectionKicker>
              <h2 id="connect-heading">معرفة مفتوحة، مع إسناد واضح لصاحب المشروع.</h2>
              <p className="lead-copy">
                المشروع مخصص للاستخدام العام والتطوير المفتوح وفق بيان المستودع. ولأن النسخة الحالية لا تعرض ترخيصًا برمجيًا منفصلًا، فالأصل هو الإحالة إلى المستودع وصاحب المشروع عند إعادة الاستخدام أو البناء عليه.
              </p>
            </div>
            <div className="stewardship-record" aria-label="بيانات الحقوق والتواصل">
              <article className="record-item record-item--repo">
                <span className="record-index">01 / المصدر</span>
                <div className="record-icon"><GithubMark /></div>
                <h3>المستودع الأصلي</h3>
                <a href="https://github.com/tareq-alomari/ibb-business-database" target="_blank" rel="noreferrer">
                  github.com/tareq-alomari/<br />ibb-business-database
                  <ExternalLink size={16} />
                </a>
              </article>
              <article className="record-item">
                <span className="record-index">02 / حقوق الاستخدام</span>
                <div className="record-icon"><BookOpenCheck size={21} /></div>
                <h3>بيان المستودع</h3>
                <p>مخصص للاستخدام العام والتطوير المفتوح، مع حفظ الإسناد إلى المشروع ومصدره.</p>
              </article>
              <article className="record-item record-item--contact">
                <span className="record-index">03 / تواصل مباشر</span>
                <div className="record-icon"><MapPinned size={21} /></div>
                <h3>طارق العمري <small>DemoSoft</small></h3>
                <a href="mailto:tareq.software.devloper@gmail.com">tareq.software.devloper@gmail.com</a>
                <a href="tel:+967715299909" dir="ltr">+967 715 299 909</a>
              </article>
            </div>
          </div>
        </section>

        <section className="closing-section" aria-labelledby="closing-heading">
          <div className="closing-contour" aria-hidden="true" />
          <div className="content-frame closing-content">
            <div className="closing-mark"><img src="/manus-storage/ibb-mark_01c90183.png" alt="" /></div>
            <p className="section-kicker section-kicker--light"><span />الخطوة التالية</p>
            <h2 id="closing-heading">البيانات المحلية ليست نهاية الطريق.<br />إنها بداية قرار أفضل.</h2>
            <p>ابدأ بقطاع واحد، وثبّت مصادره، وابنِ تجربة بحث وتحديث تخدم الناس فعلًا.</p>
            <a className="btn-light" href="#top">
              العودة إلى البداية
              <ArrowUpLeft size={18} />
            </a>
          </div>
        </section>
      </main>

      <footer className="site-footer">
        <div className="content-frame footer-inner">
          <p>© 2026 طارق العمري / DemoSoft <span>—</span> IBB Business Database.</p>
          <div className="footer-links">
            <a href="mailto:tareq.software.devloper@gmail.com">راسل صاحب المشروع</a>
            <a href="https://github.com/tareq-alomari/ibb-business-database" target="_blank" rel="noreferrer">مستودع GitHub <ExternalLink size={15} /></a>
          </div>
        </div>
      </footer>
    </div>
  );
}

function GithubMark() {
  return (
    <svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor">
      <path d="M12 1.6a10.4 10.4 0 0 0-3.29 20.27c.52.1.7-.23.7-.5v-1.8c-2.86.62-3.46-1.21-3.46-1.21-.47-1.18-1.14-1.5-1.14-1.5-.93-.63.07-.62.07-.62 1.03.07 1.57 1.05 1.57 1.05.92 1.57 2.4 1.12 2.98.86.1-.66.36-1.12.65-1.38-2.29-.26-4.7-1.14-4.7-5.1 0-1.13.4-2.05 1.05-2.77-.1-.26-.46-1.32.1-2.75 0 0 .86-.28 2.82 1.06a9.83 9.83 0 0 1 5.13 0c1.96-1.34 2.82-1.06 2.82-1.06.56 1.43.2 2.49.1 2.75.65.72 1.05 1.64 1.05 2.77 0 3.97-2.42 4.83-4.72 5.09.37.32.7.93.7 1.87v2.77c0 .28.19.61.71.5A10.4 10.4 0 0 0 12 1.6Z" />
    </svg>
  );
}
