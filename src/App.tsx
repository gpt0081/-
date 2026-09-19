import { useMemo, useState } from "react";
import { ArrowRight, BookOpen, ExternalLink, Filter, Search, ShieldCheck } from "lucide-react";

type RecordSide = {
  date: string;
  kind: string;
  text: string;
  context: string;
  source: string;
};

type Comparison = {
  id: string;
  person: string;
  role: string;
  topic: string;
  gap: string;
  past: RecordSide;
  current: RecordSide;
  explanation: string;
  note: string;
};

const comparisons: Comparison[] = [
  {
    id: "demo-001",
    person: "데모 정치인 가",
    role: "예시 데이터",
    topic: "인사 검증",
    gap: "3년 4개월",
    past: {
      date: "2022. 03. 14",
      kind: "국회 발언",
      text: "공직 후보자에게 동일한 검증 기준이 적용되어야 한다.",
      context: "상대 진영 후보자의 인사 검증을 둘러싼 공개 발언이라는 가상 예시입니다.",
      source: "데모 1차 자료",
    },
    current: {
      date: "2025. 07. 02",
      kind: "기자회견",
      text: "이번 사안은 당시와 조건이 달라 별도로 판단할 필요가 있다.",
      context: "같은 주제에 대해 상황 차이를 주장하는 가상 예시입니다.",
      source: "데모 1차 자료",
    },
    explanation: "당사자는 두 사건의 사실관계와 적용 조건이 다르다고 설명했습니다.",
    note: "같은 원칙인지, 조건 차이가 결론을 바꿀 만큼 중요한지 원문을 보고 판단합니다.",
  },
  {
    id: "demo-002",
    person: "데모 정치인 나",
    role: "예시 데이터",
    topic: "특별수사",
    gap: "2년 1개월",
    past: {
      date: "2021. 11. 08",
      kind: "인터뷰",
      text: "중대한 의혹은 독립적인 절차로 확인할 필요가 있다.",
      context: "특정 사건에 대한 독립 조사 필요성을 강조한 가상 기록입니다.",
      source: "데모 방송 원문",
    },
    current: {
      date: "2023. 12. 18",
      kind: "정책 입장",
      text: "현재 제안된 조사 방식에는 절차적 문제가 있어 동의하기 어렵다.",
      context: "조사 자체가 아니라 제안된 절차를 문제 삼는다는 가상 기록입니다.",
      source: "데모 공식 문서",
    },
    explanation: "당사자는 조사 필요성은 부정하지 않았고, 절차 설계가 문제라고 설명했습니다.",
    note: "과거 주장이 모든 형태의 조사에 대한 일반 원칙이었는지 확인해야 합니다.",
  },
  {
    id: "demo-003",
    person: "데모 정치인 다",
    role: "예시 데이터",
    topic: "선거 제도",
    gap: "4년 7개월",
    past: {
      date: "2020. 02. 21",
      kind: "정당 회의",
      text: "제도의 취지를 우회하는 방식은 바람직하지 않다.",
      context: "선거제 운용을 비판하는 가상의 정당 회의 발언입니다.",
      source: "데모 회의록",
    },
    current: {
      date: "2024. 09. 29",
      kind: "당론 발표",
      text: "현행 제도 아래에서는 경쟁 조건을 고려한 대응이 불가피하다.",
      context: "같은 제도 아래 전략적 대응 필요성을 주장하는 가상 발표입니다.",
      source: "데모 공식 발표",
    },
    explanation: "당사자는 제도 자체에 대한 비판과 현행 제도에서의 전략은 구분해야 한다고 주장했습니다.",
    note: "상대가 같은 논리를 사용했을 때도 이를 인정했는지가 추가 검토 포인트입니다.",
  },
];

const topics = ["전체", "인사 검증", "특별수사", "선거 제도"];

function App() {
  const [query, setQuery] = useState("");
  const [topic, setTopic] = useState("전체");
  const [openId, setOpenId] = useState<string | null>("demo-001");

  const filtered = useMemo(() => {
    const q = query.trim().toLowerCase();
    return comparisons.filter((item) => {
      const topicMatch = topic === "전체" || item.topic === topic;
      const queryMatch =
        !q ||
        [item.person, item.role, item.topic, item.past.text, item.current.text]
          .join(" ")
          .toLowerCase()
          .includes(q);
      return topicMatch && queryMatch;
    });
  }, [query, topic]);

  return (
    <main>
      <header className="topbar">
        <a className="brand" href="#top" aria-label="눈가리고아웅판별기 홈">
          <span className="brandMark">아웅</span>
          <span>눈가리고아웅판별기</span>
        </a>
        <nav>
          <a href="#records">기록</a>
          <a href="#method">방법론</a>
          <a href="#principles">원칙</a>
        </nav>
      </header>

      <section className="hero" id="top">
        <div className="eyebrow"><ShieldCheck size={15} /> 증거 기반 정치 기록 추적기</div>
        <h1>눈 가리고 아웅.<br /><em>기록은 눈을 감지 않는다.</em></h1>
        <p className="heroCopy">
          정치인의 과거 발언과 이후 행동을 같은 화면에 놓습니다.
          원문, 날짜, 당시 상황, 후속 설명까지 함께 보고 판단하세요.
        </p>

        <label className="searchBox">
          <Search size={21} />
          <input
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="정치인, 발언, 공약 또는 쟁점을 검색하세요"
          />
          <kbd>⌘ K</kbd>
        </label>

        <div className="manifesto">
          <span>판정 대신 기록</span>
          <span>1차 자료 우선</span>
          <span>반론도 함께</span>
          <span>자동 점수 없음</span>
        </div>
      </section>

      <section className="records" id="records">
        <div className="sectionHead">
          <div>
            <span className="kicker">DEMO ARCHIVE</span>
            <h2>앞뒤를 나란히 놓으면 보이는 것들</h2>
          </div>
          <div className="count">{filtered.length.toString().padStart(2, "0")}건</div>
        </div>

        <div className="filterRow">
          <Filter size={16} />
          {topics.map((item) => (
            <button
              key={item}
              className={topic === item ? "chip active" : "chip"}
              onClick={() => setTopic(item)}
            >
              {item}
            </button>
          ))}
        </div>

        <div className="recordList">
          {filtered.map((item) => {
            const open = openId === item.id;
            return (
              <article className="comparison" key={item.id}>
                <button className="comparisonHead" onClick={() => setOpenId(open ? null : item.id)}>
                  <div className="person">
                    <span className="avatar">{item.person.slice(-1)}</span>
                    <span>
                      <strong>{item.person}</strong>
                      <small>{item.role} · {item.topic}</small>
                    </span>
                  </div>
                  <div className="gap">
                    <small>기록 간격</small>
                    <strong>{item.gap}</strong>
                  </div>
                </button>

                <div className="split">
                  <div className="record past">
                    <div className="recordMeta"><span>과거</span>{item.past.date} · {item.past.kind}</div>
                    <blockquote>“{item.past.text}”</blockquote>
                    <div className="source"><BookOpen size={14}/>{item.past.source}</div>
                  </div>
                  <div className="arrow"><ArrowRight size={20}/></div>
                  <div className="record current">
                    <div className="recordMeta"><span>이후</span>{item.current.date} · {item.current.kind}</div>
                    <blockquote>“{item.current.text}”</blockquote>
                    <div className="source"><BookOpen size={14}/>{item.current.source}</div>
                  </div>
                </div>

                {open && (
                  <div className="contextPanel">
                    <div>
                      <b>당시 문맥</b>
                      <p>{item.past.context}</p>
                      <p>{item.current.context}</p>
                    </div>
                    <div>
                      <b>당사자 설명</b>
                      <p>{item.explanation}</p>
                    </div>
                    <div>
                      <b>검토할 질문</b>
                      <p>{item.note}</p>
                    </div>
                    <button className="sourceButton">
                      원문 묶음 보기 <ExternalLink size={14}/>
                    </button>
                  </div>
                )}
              </article>
            );
          })}
          {filtered.length === 0 && <div className="empty">조건에 맞는 비교 기록이 없습니다.</div>}
        </div>
      </section>

      <section className="method" id="method">
        <div>
          <span className="kicker">HOW IT WORKS</span>
          <h2>판별기라고 부르지만,<br />판결하지 않습니다.</h2>
        </div>
        <ol>
          <li><span>01</span><div><b>기록 수집</b><p>회의록·법안·표결·공식 발표·영상 등 원문을 우선 확보합니다.</p></div></li>
          <li><span>02</span><div><b>같은 원칙 연결</b><p>AI는 의미가 가까운 과거와 현재 기록을 ‘비교 후보’로만 연결합니다.</p></div></li>
          <li><span>03</span><div><b>문맥과 반론 병렬 표시</b><p>달라진 조건과 당사자의 해명까지 같은 비중으로 노출합니다.</p></div></li>
          <li><span>04</span><div><b>사용자가 판단</b><p>위선 점수도, 후보 순위도 없습니다. 증거를 보고 결론을 내리는 사람은 사용자입니다.</p></div></li>
        </ol>
      </section>

      <section className="principles" id="principles">
        <p>사이트의 질문은 하나입니다.</p>
        <h2>“오늘 남에게 적용한 기준을,<br />어제의 자신에게도 적용했는가?”</h2>
        <small>현재 화면의 모든 인물과 기록은 UI 검증용 가상 데이터입니다.</small>
      </section>

      <footer>
        <span>AWOONG · Political Record Tracker</span>
        <span>증거는 공개하고, 판단은 남긴다.</span>
      </footer>
    </main>
  );
}

export default App;
