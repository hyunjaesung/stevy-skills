# Stevy Skills

생각을 명료하게 만들고, 학습·투자·지식관리·의사결정을 돕는 재사용 가능한 AI 에이전트 스킬 모음입니다. 하나의 `SKILL.md` 원본을 Codex와 Claude Code에서 함께 사용합니다.

각 스킬은 개인 이름이나 특정 폴더 구조에 의존하지 않습니다. 필요한 경우 대화에서 Obsidian vault 경로와 선호 호칭을 알려주세요.

## 포함된 스킬

| 스킬 | 용도 |
|---|---|
| `grill-decisions` | 질문을 한 번에 하나씩 던져 모호한 선택을 명확한 결정으로 전환 |
| `grill-stock-decision` | 최신 공시·실적·뉴스와 다양한 투자 거장 렌즈로 매수·보유·매도 판단 점검 |
| `learn-by-redrafting` | 초안 → 학습 → 재작성 → 심문 → 최종답의 과제 중심 학습 |
| `knowledge-inbox` | 영상·글·PDF·메모를 장기 지식으로 정리하고 연결 |
| `weekly-life-scorecard` | 분기 목표와 자유형 생활 기록을 균형 잡힌 주간 점수와 다음 행동으로 전환 |

## 빠른 설치

저장소를 받은 뒤 설치 스크립트를 실행합니다.

```bash
git clone https://github.com/hyunjaesung/stevy-skills.git
cd stevy-skills
bash scripts/install.sh both all
```

첫 번째 인수는 설치 대상입니다.

```bash
bash scripts/install.sh codex all
bash scripts/install.sh claude all
bash scripts/install.sh both grill-decisions learn-by-redrafting
```

Codex는 `${CODEX_HOME:-~/.codex}/skills/`, Claude Code는 `~/.claude/skills/`에 설치됩니다. Codex는 설치 후 새 작업을 열어 목록을 갱신하세요. Claude Code는 이미 스킬 폴더를 감시 중이면 변경을 자동 감지하며, 최상위 폴더가 처음 생긴 경우 다시 시작하세요.

## 수동 설치

각 스킬 폴더는 독립적입니다. 원하는 폴더만 복사할 수 있습니다.

```bash
# Codex 개인 스킬
cp -R skills/grill-decisions ~/.codex/skills/

# Claude Code 개인 스킬
cp -R skills/grill-decisions ~/.claude/skills/

# Claude Code 프로젝트 전용 스킬
mkdir -p /path/to/project/.claude/skills
cp -R skills/grill-decisions /path/to/project/.claude/skills/
```

Claude Code에서는 관련 요청을 하면 자동으로 선택되거나 `/grill-decisions`처럼 직접 호출할 수 있습니다. 자세한 위치와 동작은 [Claude Code 공식 Skills 문서](https://code.claude.com/docs/en/skills)를 참고하세요.

## 사용 예시

- “이직할지 말지 심문해줘.”
- “이 종목 추매할까? 투자위원회 열어줘.”
- “숙제 시작하자. 공부 전후 답을 비교하고 싶어.”
- “이 유튜브 영상을 내 지식베이스에 정리해줘.”
- “이번 주에 한 일과 먹은 것을 막 적을 테니 주간 점수와 다음 주 계획을 만들어줘.”

## 설계 원칙

- 중요한 결정은 결론보다 먼저 질문과 반증을 거칩니다.
- 사실, 추정, 가정, 의견을 구분합니다.
- 금융·의료·법률처럼 시의성과 정확성이 중요한 분야는 최신 1차 자료를 우선 확인합니다.
- 사용자의 최종 결정권과 개인정보를 보호합니다.
- 장기 기억이 필요할 때만 사용자가 지정한 vault 또는 폴더에 기록합니다.

## 기여

이슈와 Pull Request를 환영합니다. 새 스킬은 `skills/<skill-name>/SKILL.md` 구조를 따르고, YAML frontmatter의 `name`과 `description`에 무엇을 하며 언제 사용해야 하는지 명확히 적어주세요. 두 플랫폼에서 함께 쓸 수 있도록 플랫폼 전용 frontmatter나 명령은 꼭 필요한 경우에만 사용합니다.

## 라이선스

[MIT License](LICENSE)
