# security

> A categorised database of **security skills for Claude Code**, aggregated from three open-source collections and organised around what you actually secure: apps, websites, APIs, cloud, and companies.

**194 skills** across **16 categories**, vendored from 3 upstream repositories. Every skill keeps its original folder, license, and attribution.

If you build apps with AI, you ship fast, and you ship blind spots. The Claude Code
community has already written hundreds of security skills that catch those blind
spots, but they live in separate repositories with different layouts, naming, and
licenses, so most people never install any of them.

This repo pulls three of the best collections into one place, sorts every skill by
the thing you are actually protecting (your web app, your logins, your secrets, your
dependencies, your cloud, your AI features), and wraps the lot in a single
marketplace you add with one command. No hunting across repos, no guessing which
skill does what.

New here? Read **Start here** below for the highest-signal checks on a vibe-coded
app, then install more by category as you need them.

Each skill is a folder of instructions (and sometimes scripts) that Claude Code loads on demand. This repo does three things: **collects** them, **categorises** them, and packages them as **one installable marketplace**.

## Sources

| Upstream | Skills | License | Pinned commit |
|---|--:|---|---|
| [trailofbits/skills](https://github.com/trailofbits/skills) | 78 | CC-BY-SA-4.0 | `321ccfe628` |
| [Masriyan/Claude-Code-CyberSecurity-Skill](https://github.com/Masriyan/Claude-Code-CyberSecurity-Skill) | 22 | MIT | `42e1501603` |
| [trilwu/secskills](https://github.com/trilwu/secskills) | 94 | MIT | `ca53957bcd` |

## Install

```bash
/plugin marketplace add gztes/security
```

Then install any plugin listed by the marketplace, e.g.:

```bash
/plugin install tob-insecure-defaults@security-skills
/plugin install trilwu-secskills-core@security-skills
/plugin install masriyan-cybersecurity@security-skills
```

> Install a few plugins for the job in front of you, not all of them at once — a smaller, relevant skill set makes Claude better at picking the right one. Skills are prompts Claude executes and some ship runnable scripts; only add what you trust.

## Start here

If you have vibe-coded an app or site and want the highest-signal checks first:

> Also install **`tob-insecure-defaults`** — a command-based plugin (hardcoded credentials, fallback secrets, dangerous defaults) that ships as a `/audit` command rather than a skill, so it is not in the table below.

| Skill | Source | What it does |
|---|---|---|
| [`differential-review`](vendored/trailofbits/plugins/differential-review/skills/differential-review/SKILL.md) | trailofbits | Performs security-focused differential review of code changes. Adapts analysis depth to codebase size, uses git blame for context, calculates blast ra |
| [`supply-chain-risk-auditor`](vendored/trailofbits/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor/SKILL.md) | trailofbits | Audits a project's dependencies for supply-chain risk: version-matched advisories for direct dependencies and the full lockfile tree, abandoned or arc |
| [`reviewing-code-changes`](vendored/trilwu/secskills-core/skills/reviewing-code-changes/SKILL.md) | trilwu | Perform a security review of a diff, branch, or pull request — assessing what the change introduces, weakens, or exposes, with a triage-first workflow |
| [`auditing-code-for-vulnerabilities`](vendored/trilwu/secskills-core/skills/auditing-code-for-vulnerabilities/SKILL.md) | trilwu | Audit source code for exploitable vulnerabilities using threat-model-driven review, taint tracing, invariant checking, and variant analysis. Use when  |
| [`Web Application Security Testing`](vendored/masriyan/skills/09-web-security/SKILL.md) | masriyan | OWASP Top 10 testing, injection vulnerability detection, API security assessment, authentication testing, and web vulnerability reporting for authoriz |
| [`Vulnerability Scanning & Assessment`](vendored/masriyan/skills/02-vulnerability-scanner/SKILL.md) | masriyan | Dependency auditing, CVE detection, configuration security review, CVSS scoring, and prioritized vulnerability reporting |
| [`securing-ai-systems`](vendored/trilwu/secskills-core/skills/securing-ai-systems/SKILL.md) | trilwu | Assess and harden LLM applications and agentic systems against prompt injection, tool misuse, excessive agency, memory poisoning, RAG data leakage, an |
| [`agentic-actions-auditor`](vendored/trailofbits/plugins/agentic-actions-auditor/skills/agentic-actions-auditor/SKILL.md) | trailofbits | Audits GitHub Actions workflows for security vulnerabilities in AI agent integrations including Claude Code Action, Gemini CLI, OpenAI Codex, and GitH |
| [`auditing-supply-chain`](vendored/trilwu/secskills-core/skills/auditing-supply-chain/SKILL.md) | trilwu | Audit software supply chain risk — dependency and transitive package review, typosquatting and dependency confusion, lockfile and SBOM analysis, CI/CD |
| [`GRC & Compliance`](vendored/masriyan/skills/19-grc-compliance/SKILL.md) | masriyan | Governance, risk, and compliance — risk assessment and scoring, control mapping across NIST CSF 2.0 / ISO 27001:2022 / SOC 2 / CIS Controls v8, gap an |

## Categories

- [AI & LLM security](#ai-llm-security) (5)
- [Smart contracts & Web3](#smart-contracts-web3) (14)
- [Fuzzing & dynamic testing](#fuzzing-dynamic-testing) (13)
- [Cryptography](#cryptography) (9)
- [Reverse engineering & binaries](#reverse-engineering-binaries) (29)
- [Incident response & forensics](#incident-response-forensics) (23)
- [Detection, hunting & threat intel](#detection-hunting-threat-intel) (19)
- [Mobile security](#mobile-security) (2)
- [Cloud, containers & Kubernetes](#cloud-containers-kubernetes) (2)
- [Dependencies & supply chain](#dependencies-supply-chain) (1)
- [Secrets & insecure defaults](#secrets-insecure-defaults) (1)
- [Code review & static analysis](#code-review-static-analysis) (19)
- [Web & API security](#web-api-security) (3)
- [Governance, risk & compliance](#governance-risk-compliance) (2)
- [Meta & workflow tooling](#meta-workflow-tooling) (11)
- [Offensive / penetration testing (authorized only)](#offensive-penetration-testing-authorized-only) (41)

### AI & LLM security

_Prompt injection, agent/tool misuse, RAG leakage, model & MCP supply chain._

| Skill | Source | What it does |
|---|---|---|
| [`AI & LLM Security`](vendored/masriyan/skills/16-ai-llm-security/SKILL.md) | masriyan | LLM and AI application security testing — prompt injection, jailbreak resistance, OWASP LLM Top 10 (2025), RAG and agent/tool-use security, model supply chain,  |
| [`agentic-actions-auditor`](vendored/trailofbits/plugins/agentic-actions-auditor/skills/agentic-actions-auditor/SKILL.md) | trailofbits | Audits GitHub Actions workflows for security vulnerabilities in AI agent integrations including Claude Code Action, Gemini CLI, OpenAI Codex, and GitHub AI Infe |
| [`auditing-mcp-servers`](vendored/trilwu/secskills-core/skills/auditing-mcp-servers/SKILL.md) | trilwu | Audit Model Context Protocol servers for injection surfaces, excessive tool scope, authorization gaps, resource over-exposure, and transport weaknesses across s |
| [`securing-ai-systems`](vendored/trilwu/secskills-core/skills/securing-ai-systems/SKILL.md) | trilwu | Assess and harden LLM applications and agentic systems against prompt injection, tool misuse, excessive agency, memory poisoning, RAG data leakage, and model su |
| [`vetting-agent-extensions`](vendored/trilwu/secskills-core/skills/vetting-agent-extensions/SKILL.md) | trilwu | Decide whether an agent skill, plugin, or MCP server is safe to install into an AI coding agent, where its content is loaded into a model's context and its conf |

### Smart contracts & Web3

_On-chain security: EVM and non-EVM contract scanners, DeFi bugs._

| Skill | Source | What it does |
|---|---|---|
| [`algorand-vulnerability-scanner`](vendored/trailofbits/plugins/building-secure-contracts/skills/algorand-vulnerability-scanner/SKILL.md) | trailofbits | Scans Algorand smart contracts for 11 common vulnerabilities including rekeying attacks, unchecked transaction fees, missing field validations, and access contr |
| [`audit-prep-assistant`](vendored/trailofbits/plugins/building-secure-contracts/skills/audit-prep-assistant/SKILL.md) | trailofbits | Prepares codebases for security review using Trail of Bits' checklist. Helps set review goals, runs static analysis tools, increases test coverage, removes dead |
| [`cairo-vulnerability-scanner`](vendored/trailofbits/plugins/building-secure-contracts/skills/cairo-vulnerability-scanner/SKILL.md) | trailofbits | Scans Cairo/StarkNet smart contracts for 6 critical vulnerabilities including felt252 arithmetic overflow, L1-L2 messaging issues, address conversion problems,  |
| [`code-maturity-assessor`](vendored/trailofbits/plugins/building-secure-contracts/skills/code-maturity-assessor/SKILL.md) | trailofbits | Systematic code maturity assessment using Trail of Bits' 9-category framework. Analyzes codebase for arithmetic safety, auditing practices, access controls, com |
| [`cosmos-vulnerability-scanner`](vendored/trailofbits/plugins/building-secure-contracts/skills/cosmos-vulnerability-scanner/SKILL.md) | trailofbits | Scans Cosmos SDK blockchain modules and CosmWasm contracts for consensus-critical vulnerabilities — chain halts, fund loss, state divergence. 25 core + 16 IBC + |
| [`entry-point-analyzer`](vendored/trailofbits/plugins/entry-point-analyzer/skills/entry-point-analyzer/SKILL.md) | trailofbits | Analyzes smart contract codebases to identify state-changing entry points for security auditing. Detects externally callable functions that modify state, catego |
| [`genotoxic`](vendored/trailofbits/plugins/trailmark/skills/genotoxic/SKILL.md) | trailofbits | Graph-informed mutation testing triage. Parses codebases with Trailmark, runs mutation testing and necessist, then uses survived mutants, unnecessary test state |
| [`guidelines-advisor`](vendored/trailofbits/plugins/building-secure-contracts/skills/guidelines-advisor/SKILL.md) | trailofbits | Smart contract development advisor based on Trail of Bits' best practices. Analyzes codebase to generate documentation/specifications, review architecture, chec |
| [`property-based-testing`](vendored/trailofbits/plugins/property-based-testing/skills/property-based-testing/SKILL.md) | trailofbits | Writes, reviews, and debugs property-based tests — Hypothesis, fast-check, proptest, jqwik, rapid, and Echidna or Medusa for Solidity invariants. Use whenever t |
| [`secure-workflow-guide`](vendored/trailofbits/plugins/building-secure-contracts/skills/secure-workflow-guide/SKILL.md) | trailofbits | Guides through Trail of Bits' 5-step secure development workflow. Runs Slither scans, checks special features (upgradeability/ERC conformance/token integration) |
| [`solana-vulnerability-scanner`](vendored/trailofbits/plugins/building-secure-contracts/skills/solana-vulnerability-scanner/SKILL.md) | trailofbits | Scans Solana programs for 6 critical vulnerabilities including arbitrary CPI, improper PDA validation, missing signer/ownership checks, and sysvar spoofing. Use |
| [`substrate-vulnerability-scanner`](vendored/trailofbits/plugins/building-secure-contracts/skills/substrate-vulnerability-scanner/SKILL.md) | trailofbits | Scans Substrate/Polkadot pallets for 7 critical vulnerabilities including arithmetic overflow, panic DoS, incorrect weights, and bad origin checks. Use when aud |
| [`token-integration-analyzer`](vendored/trailofbits/plugins/building-secure-contracts/skills/token-integration-analyzer/SKILL.md) | trailofbits | Token integration and implementation analyzer based on Trail of Bits' token integration checklist. Analyzes token implementations for ERC20/ERC721 conformity, c |
| [`ton-vulnerability-scanner`](vendored/trailofbits/plugins/building-secure-contracts/skills/ton-vulnerability-scanner/SKILL.md) | trailofbits | Scans TON (The Open Network) smart contracts for 3 critical vulnerabilities including integer-as-boolean misuse, fake Jetton contracts, and forward TON without  |

### Fuzzing & dynamic testing

_libFuzzer, AFL++, Atheris, cargo-fuzz, sanitizers, coverage, harnesses._

| Skill | Source | What it does |
|---|---|---|
| [`address-sanitizer`](vendored/trailofbits/plugins/testing-handbook-skills/skills/address-sanitizer/SKILL.md) | trailofbits | Builds and runs code under AddressSanitizer to catch buffer overflows, use-after-free, and other memory errors during fuzzing or tests. Covers -fsanitize=addres |
| [`aflpp`](vendored/trailofbits/plugins/testing-handbook-skills/skills/aflpp/SKILL.md) | trailofbits | Sets up and runs AFL++ for multi-core fuzzing of C/C++ projects built with afl-clang-fast or afl-gcc-fast. Covers instrumentation modes, parallel main and secon |
| [`atheris`](vendored/trailofbits/plugins/testing-handbook-skills/skills/atheris/SKILL.md) | trailofbits | Sets up and runs Atheris, the coverage-guided Python fuzzer built on libFuzzer. Covers TestOneInput harnesses, FuzzedDataProvider, instrumenting both pure Pytho |
| [`cargo-fuzz`](vendored/trailofbits/plugins/testing-handbook-skills/skills/cargo-fuzz/SKILL.md) | trailofbits | Sets up and runs cargo-fuzz, the standard fuzzing tool for Cargo-based Rust projects. Covers cargo fuzz init, the nightly toolchain requirement, fuzz_target! ha |
| [`coverage-analysis`](vendored/trailofbits/plugins/testing-handbook-skills/skills/coverage-analysis/SKILL.md) | trailofbits | Measures and interprets what a fuzzing campaign actually reaches, using llvm-cov, lcov, or a fuzzer's own coverage output. Covers baselining a new campaign, rea |
| [`fuzzing-dictionary`](vendored/trailofbits/plugins/testing-handbook-skills/skills/fuzzing-dictionary/SKILL.md) | trailofbits | Builds and applies fuzzing dictionaries so a fuzzer can produce the keywords, magic bytes, and tokens a target expects. Covers extracting tokens from source, he |
| [`fuzzing-obstacles`](vendored/trailofbits/plugins/testing-handbook-skills/skills/fuzzing-obstacles/SKILL.md) | trailofbits | Patches past the barriers that stop a fuzzer making progress — checksum and hash verification, magic-value validation, time-based seeds, and other non-determini |
| [`harness-writing`](vendored/trailofbits/plugins/testing-handbook-skills/skills/harness-writing/SKILL.md) | trailofbits | Designs and improves fuzzing harnesses for C/C++ and Rust. Covers mapping raw bytes onto a target API, generating structured inputs, avoiding non-determinism an |
| [`libafl`](vendored/trailofbits/plugins/testing-handbook-skills/skills/libafl/SKILL.md) | trailofbits | Builds custom fuzzers with LibAFL, the modular Rust fuzzing library. Covers composing observers, feedbacks, mutators, schedulers, and executors into a fuzzer fo |
| [`libfuzzer`](vendored/trailofbits/plugins/testing-handbook-skills/skills/libfuzzer/SKILL.md) | trailofbits | Sets up and runs libFuzzer, the coverage-guided fuzzer built into LLVM, on C/C++ code that compiles with Clang. Covers harness structure, -fsanitize=fuzzer buil |
| [`ossfuzz`](vendored/trailofbits/plugins/testing-handbook-skills/skills/ossfuzz/SKILL.md) | trailofbits | Enrolls a project in OSS-Fuzz, Google's free continuous fuzzing service for open source, and drives it locally. Covers project.yaml, Dockerfile and build.sh set |
| [`reversing-network-protocols`](vendored/trilwu/secskills-core/skills/reversing-network-protocols/SKILL.md) | trilwu | Reverse engineer undocumented binary network protocols from packet captures and the client that speaks them — recovering framing and field structure, identifyin |
| [`ruzzy`](vendored/trailofbits/plugins/testing-handbook-skills/skills/ruzzy/SKILL.md) | trailofbits | Sets up and runs Ruzzy, Trail of Bits' coverage-guided Ruby fuzzer and the only production-ready one for the language. Covers harness structure, fuzzing pure Ru |

### Cryptography

_Crypto misuse, constant-time analysis, TLS, formal proofs._

| Skill | Source | What it does |
|---|---|---|
| [`Cryptographic Analysis & Assessment`](vendored/masriyan/skills/13-crypto-analysis/SKILL.md) | masriyan | SSL/TLS auditing, cipher suite analysis, hash algorithm identification, encryption implementation review, and cryptographic weakness detection in code |
| [`constant-time-analysis`](vendored/trailofbits/plugins/constant-time-analysis/skills/constant-time-analysis/SKILL.md) | trailofbits | Detects timing side-channel vulnerabilities in cryptographic code. Use when implementing or reviewing crypto code, encountering division on secrets, secret-depe |
| [`constant-time-testing`](vendored/trailofbits/plugins/testing-handbook-skills/skills/constant-time-testing/SKILL.md) | trailofbits | Measures timing side channels in cryptographic implementations by running them, using dudect for statistical analysis and Timecop over Valgrind for dynamic trac |
| [`crypto-protocol-diagram`](vendored/trailofbits/plugins/trailmark/skills/crypto-protocol-diagram/SKILL.md) | trailofbits | Extracts protocol message flow from source code, RFCs, academic papers, pseudocode, informal prose, ProVerif (.pv), or Tamarin (.spthy) models and generates Mer |
| [`mermaid-to-proverif`](vendored/trailofbits/plugins/trailmark/skills/mermaid-to-proverif/SKILL.md) | trailofbits | Translates Mermaid sequenceDiagrams describing cryptographic protocols into ProVerif formal verification models (.pv files). Use when generating a ProVerif mode |
| [`reviewing-cryptography`](vendored/trilwu/secskills-core/skills/reviewing-cryptography/SKILL.md) | trilwu | Review cryptographic implementations and protocol usage for misuse — weak primitives, nonce and IV handling, key management, authentication of ciphertext, rando |
| [`vector-forge`](vendored/trailofbits/plugins/trailmark/skills/vector-forge/SKILL.md) | trailofbits | Mutation-driven test vector generation. Finds implementations of a cryptographic algorithm or protocol, runs mutation testing to identify escaped mutants, then  |
| [`writing-lean-proofs`](vendored/trailofbits/plugins/writing-lean-proofs/skills/writing-lean-proofs/SKILL.md) | trailofbits | Writes and reviews structured Lean 4 proofs and designs Lean libraries following Mathlib conventions. Use when proving theorems in Lean, formalizing mathematics |
| [`wycheproof`](vendored/trailofbits/plugins/testing-handbook-skills/skills/wycheproof/SKILL.md) | trailofbits | Validates cryptographic implementations against Project Wycheproof's test vectors, which encode known attacks and edge cases across AES, RSA, ECDSA, ECDH, and m |

### Reverse engineering & binaries

_Disassembly, decompilation, firmware, packers, obfuscation, protocols._

| Skill | Source | What it does |
|---|---|---|
| [`Reverse Engineering & Binary Analysis`](vendored/masriyan/skills/04-reverse-engineering/SKILL.md) | masriyan | Binary analysis, assembly interpretation, disassembly, decompilation, firmware RE, and protocol reverse engineering |
| [`analyzing-binaries`](vendored/trilwu/secskills-core/skills/analyzing-binaries/SKILL.md) | trilwu | Reverse engineer compiled binaries, firmware, and mobile app packages using triage, static disassembly, decompilation, and dynamic instrumentation. Use when ana |
| [`analyzing-dotnet-assemblies`](vendored/trilwu/secskills-core/skills/analyzing-dotnet-assemblies/SKILL.md) | trilwu | Reverse engineer .NET assemblies and executables with dnSpyEx, ILSpy, and de4dot — identifying and unwrapping obfuscators and packers, deobfuscating control flo |
| [`analyzing-firmware-images`](vendored/trilwu/secskills-core/skills/analyzing-firmware-images/SKILL.md) | trilwu | Extract, analyze, and assess firmware images from embedded devices, IoT hardware, routers, and similar targets — filesystem extraction, hardcoded credential dis |
| [`analyzing-go-binaries`](vendored/trilwu/secskills-core/skills/analyzing-go-binaries/SKILL.md) | trilwu | Reverse engineer Go binaries by recovering function names and types from pclntab and moduledata using GoReSym, redress, and IDA/Ghidra Go plugins, and by readin |
| [`analyzing-ios-binaries`](vendored/trilwu/secskills-core/skills/analyzing-ios-binaries/SKILL.md) | trilwu | Analyze iOS applications at the binary level — decrypting FairPlay-protected IPAs with frida-ios-dump or bagbak, inspecting Mach-O load commands, recovering Obj |
| [`analyzing-macos-binaries`](vendored/trilwu/secskills-core/skills/analyzing-macos-binaries/SKILL.md) | trilwu | Reverse engineer and security-review macOS applications and Mach-O binaries — thinning universal binaries, recovering Objective-C/Swift structure, reading code- |
| [`analyzing-malware`](vendored/trilwu/secskills-defense/skills/analyzing-malware/SKILL.md) | trilwu | Analyze suspected malware safely — containment, static triage, sandboxed detonation, unpacking, capability and C2 extraction, IOC production, and YARA rule auth |
| [`analyzing-rust-binaries`](vendored/trilwu/secskills-core/skills/analyzing-rust-binaries/SKILL.md) | trilwu | Reverse engineer Rust binaries — demangling legacy and v0 symbol schemes, recognizing monomorphized generics, Result and Option control flow, trait object vtabl |
| [`audit-augmentation`](vendored/trailofbits/plugins/trailmark/skills/audit-augmentation/SKILL.md) | trailofbits | > Augments Trailmark code graphs with external audit findings from SARIF static analysis results, weAudit annotation files, and version-gated Trailmark 0.4.x bi |
| [`devirtualizing-vm-protected-code`](vendored/trilwu/secskills-core/skills/devirtualizing-vm-protected-code/SKILL.md) | trilwu | Recover the original logic from code protected by a virtualization obfuscator — VMProtect, Themida/WinLicense, Code Virtualizer, or a custom opcode VM — by loca |
| [`diagramming-code`](vendored/trailofbits/plugins/trailmark/skills/diagramming-code/SKILL.md) | trailofbits | > Generates Mermaid diagrams from Trailmark code graphs. Produces call graphs, class hierarchies, module dependency maps, containment diagrams, complexity heatm |
| [`diffing-binary-patches`](vendored/trilwu/secskills-core/skills/diffing-binary-patches/SKILL.md) | trilwu | Locate the vulnerability a security patch fixes by diffing the pre- and post-patch binaries — using BinDiff, Diaphora, or ghidriff to find the changed functions |
| [`dwarf-expert`](vendored/trailofbits/plugins/dwarf-expert/skills/dwarf-expert/SKILL.md) | trailofbits | Analyzes DWARF debug information in compiled binaries. Use when inspecting .debug_* sections, DIE trees, or DW_TAG_/DW_AT_ entries with dwarfdump/llvm-dwarfdump |
| [`graph-evolution`](vendored/trailofbits/plugins/trailmark/skills/graph-evolution/SKILL.md) | trailofbits | > Compares Trailmark code graphs at two source code snapshots (git commits, tags, or directories) to surface security-relevant structural changes. Detects new a |
| [`reversing-browser-extensions`](vendored/trilwu/secskills-core/skills/reversing-browser-extensions/SKILL.md) | trilwu | Reverse engineer and security-review Chrome/Firefox browser extensions — unpacking the CRX/XPI, reading the manifest for over-broad permissions, and tracing the |
| [`reversing-flutter-apps`](vendored/trilwu/secskills-core/skills/reversing-flutter-apps/SKILL.md) | trilwu | Reverse engineer and intercept traffic from Flutter/Dart mobile apps using blutter, reFlutter, and Frida. Use when an APK or IPA contains libflutter.so, libapp. |
| [`reversing-obfuscated-javascript`](vendored/trilwu/secskills-core/skills/reversing-obfuscated-javascript/SKILL.md) | trilwu | Reverse engineer minified, bundled, and obfuscated browser/Node JavaScript — unpacking webpack chunks, recovering source from sourcemaps, undoing obfuscator.io  |
| [`reversing-react-native-apps`](vendored/trilwu/secskills-core/skills/reversing-react-native-apps/SKILL.md) | trilwu | Reverse engineer React Native mobile apps, including Hermes bytecode bundles, using hbctool, hermes-dec, and Frida. Use when an APK contains index.android.bundl |
| [`reversing-unity-il2cpp`](vendored/trilwu/secskills-core/skills/reversing-unity-il2cpp/SKILL.md) | trilwu | Reverse engineer Unity games and apps built with IL2CPP or Mono, using Il2CppDumper, Il2CppInspector, and dnSpy. Use when an APK or IPA contains global-metadata |
| [`reversing-xamarin-maui`](vendored/trilwu/secskills-core/skills/reversing-xamarin-maui/SKILL.md) | trilwu | Reverse engineer Xamarin and .NET MAUI mobile apps by extracting assemblies.blob and XALZ-compressed DLLs with pyxamstore, then decompiling with dnSpy or ILSpy. |
| [`slicing-code-context`](vendored/trailofbits/plugins/trailmark/skills/slicing-code-context/SKILL.md) | trailofbits | Selects bounded, graph-informed source slices with Trailmark and delegates focused code analysis or patch-proposal work to a smaller subagent. Use when offloadi |
| [`trailmark`](vendored/trailofbits/plugins/trailmark/skills/trailmark/SKILL.md) | trailofbits | Builds and queries multi-language source and binary code graphs for security analysis. Includes pre-analysis passes for blast radius, taint propagation, privile |
| [`trailmark-finding-triage`](vendored/trailofbits/plugins/trailmark/skills/trailmark-finding-triage/SKILL.md) | trailofbits | Performs graph-assisted triage of a single security finding, SARIF result, weAudit annotation, suspicious function, or report excerpt using Trailmark reachabili |
| [`trailmark-review-gate`](vendored/trailofbits/plugins/trailmark/skills/trailmark-review-gate/SKILL.md) | trailofbits | Runs a Trailmark structural review gate over a branch, pull request, fix commit, release diff, or git ref range to detect new entrypoints, new tainted paths, re |
| [`trailmark-structural`](vendored/trailofbits/plugins/trailmark/skills/trailmark-structural/SKILL.md) | trailofbits | Runs full Trailmark structural analysis by building a graph, running `preanalysis()`, and reporting hotspots, taint, blast radius, privilege boundaries, attack  |
| [`trailmark-summary`](vendored/trailofbits/plugins/trailmark/skills/trailmark-summary/SKILL.md) | trailofbits | Runs a Trailmark summary analysis on a codebase. Returns auto-detected languages, entry point count, and dependency list. Use when vivisect or galvanize needs a |
| [`trailmark-variant-neighborhood`](vendored/trailofbits/plugins/trailmark/skills/trailmark-variant-neighborhood/SKILL.md) | trailofbits | Expands one confirmed or suspected vulnerability into a Trailmark graph neighborhood of variant candidates by finding sibling functions, shared callers and call |
| [`unpacking-protected-binaries`](vendored/trilwu/secskills-core/skills/unpacking-protected-binaries/SKILL.md) | trilwu | Unpack and dump protected executables — UPX and commodity packers, custom crypters, commercial protectors like Themida and VMProtect, and .NET packers — by find |

### Incident response & forensics

_DFIR: triage, memory/disk/network forensics, malware, cloud incident investigation._

| Skill | Source | What it does |
|---|---|---|
| [`CSOC Operations & Playbook Automation`](vendored/masriyan/skills/11-csoc-automation/SKILL.md) | masriyan | SOC alert triage, incident playbook automation, escalation workflows, shift reporting, and SOC KPI tracking |
| [`Exploit Development & Payload Engineering`](vendored/masriyan/skills/03-exploit-development/SKILL.md) | masriyan | Proof-of-concept development, payload crafting, shellcode analysis, and exploitation technique research for authorized security testing |
| [`Incident Response & Digital Forensics`](vendored/masriyan/skills/07-incident-response/SKILL.md) | masriyan | IR playbook execution, evidence collection, forensic timeline analysis, memory forensics, and post-incident reporting following NIST SP 800-61 and SANS PICERL m |
| [`Log Analysis & SIEM Integration`](vendored/masriyan/skills/12-log-analysis/SKILL.md) | masriyan | Security log parsing, anomaly detection, SIEM query building, Sigma rule creation, and correlation rule development across Splunk, Elastic, QRadar, and Microsof |
| [`Malware Analysis & Sandboxing`](vendored/masriyan/skills/05-malware-analysis/SKILL.md) | masriyan | Static and dynamic malware analysis, YARA rule generation, sandbox configuration, behavioral profiling, and malware family classification |
| [`Mobile Application Security`](vendored/masriyan/skills/17-mobile-security/SKILL.md) | masriyan | Android and iOS application security testing — static and dynamic analysis, APK/IPA inspection, OWASP MASVS/MASTG verification, secure-storage and transport rev |
| [`analyzing-disk-images`](vendored/trilwu/secskills-defense/skills/analyzing-disk-images/SKILL.md) | trilwu | Perform dead-disk forensics on an acquired disk image using The Sleuth Kit, Plaso, and bulk_extractor — verify integrity and mount read-only, map partitions, re |
| [`analyzing-linux-persistence`](vendored/trilwu/secskills-defense/skills/analyzing-linux-persistence/SKILL.md) | trilwu | Systematically identify and analyze persistence mechanisms on Linux systems during DFIR investigations -- sweep systemd units, cron jobs, shell initialization,  |
| [`analyzing-memory-images`](vendored/trilwu/secskills-defense/skills/analyzing-memory-images/SKILL.md) | trilwu | Analyze volatile memory images (RAM dumps) using Volatility 3 — process enumeration, injected code detection, credential extraction, network artifacts, rootkit  |
| [`analyzing-network-traffic`](vendored/trilwu/secskills-defense/skills/analyzing-network-traffic/SKILL.md) | trilwu | Analyze packet captures and network telemetry for intrusion evidence — capture and handling, the Wireshark/tshark triage funnel, Zeek log mining, Suricata rule  |
| [`analyzing-phishing-emails`](vendored/trilwu/secskills-defense/skills/analyzing-phishing-emails/SKILL.md) | trilwu | Triage and forensically analyze reported phishing safely — extract the raw message, read the Received chain, verify SPF/DKIM/DMARC, detect display-name and look |
| [`analyzing-shellcode`](vendored/trilwu/secskills-defense/skills/analyzing-shellcode/SKILL.md) | trilwu | Analyze raw shellcode and position-independent code — extracting the bytes, guessing architecture, disassembling at the right base, decoding self-decoder stubs, |
| [`auditing-supply-chain`](vendored/trilwu/secskills-core/skills/auditing-supply-chain/SKILL.md) | trilwu | Audit software supply chain risk — dependency and transitive package review, typosquatting and dependency confusion, lockfile and SBOM analysis, CI/CD pipeline  |
| [`hunting-web-backdoors`](vendored/trilwu/secskills-core/skills/hunting-web-backdoors/SKILL.md) | trilwu | Hunt planted webshells and backdoors across a web source tree — PHP first (also JSP, ASP, Node) — triaging a directory at scale, statically decoding obfuscation |
| [`investigating-aws-incidents`](vendored/trilwu/secskills-defense/skills/investigating-aws-incidents/SKILL.md) | trilwu | Investigate security incidents in Amazon Web Services -- reconstruct attacker activity from CloudTrail, VPC Flow Logs, and GuardDuty, anchor the investigation o |
| [`investigating-azure-incidents`](vendored/trilwu/secskills-defense/skills/investigating-azure-incidents/SKILL.md) | trilwu | Investigate security incidents in Microsoft Azure (resource and subscription control plane) -- reconstruct attacker activity from the Azure Activity Log and res |
| [`investigating-gcp-incidents`](vendored/trilwu/secskills-defense/skills/investigating-gcp-incidents/SKILL.md) | trilwu | Investigate a security incident in Google Cloud — establishing what audit logging exists before trusting a gap, reconstructing activity from Cloud Audit Logs, t |
| [`investigating-m365-entra`](vendored/trilwu/secskills-defense/skills/investigating-m365-entra/SKILL.md) | trilwu | Investigate security incidents in Microsoft 365 and Entra ID (Azure AD) -- search the Unified Audit Log, correlate sign-in and audit events, trace illicit OAuth |
| [`investigating-windows-endpoints`](vendored/trilwu/secskills-defense/skills/investigating-windows-endpoints/SKILL.md) | trilwu | Investigate a compromised or suspicious Windows host from on-disk artifacts -- triage collection, evidence of execution (Prefetch, Amcache, Shimcache, SRUM, Use |
| [`responding-to-incidents`](vendored/trilwu/secskills-defense/skills/responding-to-incidents/SKILL.md) | trilwu | Run digital forensics and incident response — triage, evidence acquisition with chain of custody, host and cloud artifact analysis, timeline reconstruction, sco |
| [`triaging-security-alerts`](vendored/trilwu/secskills-defense/skills/triaging-security-alerts/SKILL.md) | trilwu | Work a security alert queue to a defensible disposition — separating true positives from false positives and benign true positives, reasoning about base rates b |
| [`writing-yara-rules`](vendored/trilwu/secskills-defense/skills/writing-yara-rules/SKILL.md) | trilwu | Author durable YARA detection rules — meta/strings/condition anatomy, string types and modifiers, structural conditions with file magic and offsets, the PE/ELF/ |
| [`yara-rule-authoring`](vendored/trailofbits/plugins/yara-authoring/skills/yara-rule-authoring/SKILL.md) | trailofbits | > Guides authoring of high-quality YARA-X detection rules for malware identification. Use when writing, reviewing, or optimizing YARA rules. Covers naming conve |

### Detection, hunting & threat intel

_Detection engineering, Sigma/YARA, threat hunting, CTI, defensive hardening._

| Skill | Source | What it does |
|---|---|---|
| [`Blue Team Defense & Hardening`](vendored/masriyan/skills/15-blue-team-defense/SKILL.md) | masriyan | System hardening, detection engineering, security baseline monitoring, patch management, defense-in-depth architecture, and security posture improvement |
| [`Network Security & Traffic Analysis`](vendored/masriyan/skills/08-network-security/SKILL.md) | masriyan | Network traffic analysis, PCAP parsing, IDS/IPS rule creation, firewall configuration auditing, and network anomaly detection |
| [`Purple Team & Adversary Emulation`](vendored/masriyan/skills/22-purple-team/SKILL.md) | masriyan | Collaborative purple-team operations — threat-informed adversary emulation planning (ATT&CK, CTID, Atomic Red Team, CALDERA), the detect-tune-validate loop, det |
| [`Supply Chain Security`](vendored/masriyan/skills/20-supply-chain-security/SKILL.md) | masriyan | Software supply chain security — SBOM generation and analysis, dependency confusion and typosquatting detection, malicious package indicators, CI/CD pipeline ha |
| [`Threat Hunting & IOC Analysis`](vendored/masriyan/skills/06-threat-hunting/SKILL.md) | masriyan | IOC extraction, threat intelligence correlation, MITRE ATT&CK mapping, hunt hypothesis generation, and detection rule creation |
| [`Threat Intelligence & CTI`](vendored/masriyan/skills/21-threat-intelligence/SKILL.md) | masriyan | Cyber threat intelligence production — the intelligence cycle, IOC extraction/normalization/enrichment, STIX/TAXII and MISP, structured analytic models (Diamond |
| [`Vulnerability Scanning & Assessment`](vendored/masriyan/skills/02-vulnerability-scanner/SKILL.md) | masriyan | Dependency auditing, CVE detection, configuration security review, CVSS scoring, and prioritized vulnerability reporting |
| [`Web Application Security Testing`](vendored/masriyan/skills/09-web-security/SKILL.md) | masriyan | OWASP Top 10 testing, injection vulnerability detection, API security assessment, authentication testing, and web vulnerability reporting for authorized assessm |
| [`defending-kubernetes`](vendored/trilwu/secskills-defense/skills/defending-kubernetes/SKILL.md) | trilwu | Harden and monitor a Kubernetes cluster against the attacks that actually happen — RBAC least privilege and escalation paths, Pod Security Admission enforcement |
| [`engineering-detections`](vendored/trilwu/secskills-defense/skills/engineering-detections/SKILL.md) | trilwu | Build, test, and tune detection content — Sigma, YARA, Suricata, and EDR/SIEM queries — mapped to MITRE ATT&CK with explicit false-positive analysis and detecti |
| [`hardening-cloud-posture`](vendored/trilwu/secskills-defense/skills/hardening-cloud-posture/SKILL.md) | trilwu | Proactively harden a cloud account or organization before an incident — prioritizing IAM and identity risk over checkbox findings, closing the exposures that be |
| [`hunting-threats`](vendored/trilwu/secskills-defense/skills/hunting-threats/SKILL.md) | trilwu | Run hypothesis-driven threat hunts across endpoint, network, cloud, and identity telemetry using stack counting, outlier analysis, and ATT&CK-based hypotheses,  |
| [`managing-vulnerabilities`](vendored/trilwu/secskills-defense/skills/managing-vulnerabilities/SKILL.md) | trilwu | Prioritize and drive remediation of a vulnerability backlog by real risk, not raw CVSS — combining severity with exploitation signals (EPSS, CISA KEV), asset ex |
| [`mapping-attack-techniques`](vendored/trilwu/secskills-core/skills/mapping-attack-techniques/SKILL.md) | trilwu | Navigate security work by MITRE ATT&CK tactic and technique — resolve a technique ID or name to the right skill, map a threat intel report or adversary emulatio |
| [`producing-threat-intelligence`](vendored/trilwu/secskills-defense/skills/producing-threat-intelligence/SKILL.md) | trilwu | Produce cyber threat intelligence by pivoting on indicators to find related infrastructure, tracking actors and campaigns, enriching and contextualizing IOCs, a |
| [`sarif-parsing`](vendored/trailofbits/plugins/static-analysis/skills/sarif-parsing/SKILL.md) | trailofbits | >- Parses and processes SARIF files from static analysis tools like CodeQL, Semgrep, or other scanners. Triggers on "parse sarif", "read scan results", "aggrega |
| [`semgrep-rule-creator`](vendored/trailofbits/plugins/semgrep-rule-creator/skills/semgrep-rule-creator/SKILL.md) | trailofbits | Creates custom Semgrep rules for detecting security vulnerabilities, bug patterns, and code patterns. Use when writing Semgrep rules or building custom static a |
| [`testing-mobile-applications`](vendored/trilwu/secskills-offense/skills/testing-mobile-applications/SKILL.md) | trilwu | Pentest Android and iOS mobile applications including APK analysis, dynamic analysis, SSL pinning bypass, root/jailbreak detection bypass, and mobile-specific v |
| [`writing-sigma-rules`](vendored/trilwu/secskills-defense/skills/writing-sigma-rules/SKILL.md) | trilwu | Author and maintain Sigma detection rules — structure, logsource taxonomy, detection logic with modifiers, false-positive filtering, backend conversion with pyS |

### Mobile security

_Android/iOS app testing, pinning bypass, mobile IPC._

| Skill | Source | What it does |
|---|---|---|
| [`firebase-apk-scanner`](vendored/trailofbits/plugins/firebase-apk-scanner/skills/firebase-apk-scanner/SKILL.md) | trailofbits | Scans Android APKs for Firebase security misconfigurations including open databases, storage buckets, authentication issues, and exposed cloud functions. Use wh |
| [`testing-mobile-ipc`](vendored/trilwu/secskills-offense/skills/testing-mobile-ipc/SKILL.md) | trilwu | Test mobile inter-process communication and deep link attack surface — exported Android activities, services, receivers and content providers, intent redirectio |

### Cloud, containers & Kubernetes

_AWS/Azure/GCP, Docker, and Kubernetes posture and hardening._

| Skill | Source | What it does |
|---|---|---|
| [`Cloud Security & Container Hardening`](vendored/masriyan/skills/10-cloud-security/SKILL.md) | masriyan | AWS/Azure/GCP security auditing, container and Kubernetes hardening, Infrastructure as Code scanning, and cloud compliance assessment |
| [`devcontainer-setup`](vendored/trailofbits/plugins/devcontainer-setup/skills/devcontainer-setup/SKILL.md) | trailofbits | Creates devcontainers with Claude Code, language-specific tooling (Python/Node/Rust/Go), and persistent volumes. Use when adding devcontainer support to a proje |

### Dependencies & supply chain

_Third-party package risk, SBOMs, typosquatting, CI/CD and OIDC trust._

| Skill | Source | What it does |
|---|---|---|
| [`supply-chain-risk-auditor`](vendored/trailofbits/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor/SKILL.md) | trailofbits | Audits a project's dependencies for supply-chain risk: version-matched advisories for direct dependencies and the full lockfile tree, abandoned or archived upst |

### Secrets & insecure defaults

_Hardcoded credentials, fallback secrets, dangerous default configuration, zeroization._

| Skill | Source | What it does |
|---|---|---|
| [`zeroize-audit`](vendored/trailofbits/plugins/zeroize-audit/skills/zeroize-audit/SKILL.md) | trailofbits | Detects missing zeroization of sensitive data in source code and identifies zeroization removed by compiler optimizations, with assembly-level analysis, and con |

### Code review & static analysis

_Diff review, language security review, SAST, semgrep/codeql, property & mutation testing._

| Skill | Source | What it does |
|---|---|---|
| [`audit-context-building`](vendored/trailofbits/plugins/audit-context-building/skills/audit-context-building/SKILL.md) | trailofbits | Understand a codebase before looking for bugs in it - what each function assumes, what it guarantees, and what it depends on elsewhere. Use when starting an aud |
| [`auditing-code-for-vulnerabilities`](vendored/trilwu/secskills-core/skills/auditing-code-for-vulnerabilities/SKILL.md) | trilwu | Audit source code for exploitable vulnerabilities using threat-model-driven review, taint tracing, invariant checking, and variant analysis. Use when reviewing  |
| [`auditing-php-applications`](vendored/trilwu/secskills-core/skills/auditing-php-applications/SKILL.md) | trilwu | Audit PHP web application source for critical vulnerabilities using PHP's specific sink and footgun catalog — object injection via unserialize and phar:// POP c |
| [`c-review`](vendored/trailofbits/plugins/c-review/skills/c-review/SKILL.md) | trailofbits | Performs comprehensive C/C++ security review for memory corruption, integer overflows, race conditions, and platform-specific vulnerabilities. Use when auditing |
| [`codeql`](vendored/trailofbits/plugins/static-analysis/skills/codeql/SKILL.md) | trailofbits | >- Scans a codebase for security vulnerabilities using CodeQL's interprocedural data flow and taint tracking analysis. Triggers on "run codeql", "codeql scan",  |
| [`differential-review`](vendored/trailofbits/plugins/differential-review/skills/differential-review/SKILL.md) | trailofbits | Performs security-focused differential review of code changes. Adapts analysis depth to codebase size, uses git blame for context, calculates blast radius by co |
| [`dimensional-analysis`](vendored/trailofbits/plugins/dimensional-analysis/skills/dimensional-analysis/SKILL.md) | trailofbits | Annotates codebases with dimensional analysis comments documenting units, dimensions, and decimal scaling. Use when someone asks to annotate units in a codebase |
| [`fp-check`](vendored/trailofbits/plugins/fp-check/skills/fp-check/SKILL.md) | trailofbits | Systematically verifies suspected security bugs to eliminate false positives, producing a TRUE POSITIVE or FALSE POSITIVE verdict with documented evidence for e |
| [`modern-cpp`](vendored/trailofbits/plugins/modern-cpp/skills/modern-cpp/SKILL.md) | trailofbits | Guides C++ code toward modern idioms (C++20/23/26). Use when writing new C++ code, modernizing legacy patterns, or working on security-critical C++. Replaces ra |
| [`modern-python`](vendored/trailofbits/plugins/modern-python/skills/modern-python/SKILL.md) | trailofbits | Configures Python projects with modern tooling (uv, ruff, ty). Use when creating projects, writing standalone scripts, or migrating from pip/Poetry/mypy/black. |
| [`mutation-testing`](vendored/trailofbits/plugins/mutation-testing/skills/mutation-testing/SKILL.md) | trailofbits | Configures mewt or muton mutation testing campaigns — scopes targets, tunes timeouts, and optimizes long-running runs. Use when the user mentions mewt, muton, m |
| [`reviewing-code-changes`](vendored/trilwu/secskills-core/skills/reviewing-code-changes/SKILL.md) | trilwu | Perform a security review of a diff, branch, or pull request — assessing what the change introduces, weakens, or exposes, with a triage-first workflow and false |
| [`rust-review`](vendored/trailofbits/plugins/rust-review/skills/rust-review/SKILL.md) | trailofbits | Performs comprehensive Rust security review for safe/unsafe boundary issues, memory safety in unsafe blocks, concurrency hazards, panic-induced DoS, FFI safety, |
| [`semgrep`](vendored/trailofbits/plugins/static-analysis/skills/semgrep/SKILL.md) | trailofbits | >- Runs a Semgrep security scan over a codebase: detects languages, selects rulesets, presents the plan for explicit approval, then runs every approved ruleset  |
| [`semgrep-rule-variant-creator`](vendored/trailofbits/plugins/semgrep-rule-variant-creator/skills/semgrep-rule-variant-creator/SKILL.md) | trailofbits | Creates language variants of existing Semgrep rules. Use when porting a Semgrep rule to specified target languages. Takes an existing rule and target languages  |
| [`sharp-edges`](vendored/trailofbits/plugins/sharp-edges/skills/sharp-edges/SKILL.md) | trailofbits | Identifies error-prone APIs, dangerous configurations, and footgun designs that enable security mistakes. Use when reviewing API designs, configuration schemas, |
| [`spec-to-code-compliance`](vendored/trailofbits/plugins/spec-to-code-compliance/skills/spec-to-code-compliance/SKILL.md) | trailofbits | Check code against the documentation that specifies it - which requirements hold, which the code contradicts, which are absent, and what the code does that no d |
| [`variant-analysis`](vendored/trailofbits/plugins/variant-analysis/skills/variant-analysis/SKILL.md) | trailofbits | Hunts for the other instances of a bug already found — the variants of one root cause across a codebase. Use immediately after a vulnerability, logic bug, or ba |
| [`vulnerability-triage-brocards`](vendored/trailofbits/plugins/vulnerability-triage-brocards/skills/vulnerability-triage-brocards/SKILL.md) | trailofbits | >- This skill should be used when the user asks to "triage a vulnerability report", "assess a CVE", "evaluate a bug bounty submission", "decide if a finding is  |

### Web & API security

_OWASP-style testing and review of web apps and APIs — the bugs vibe-coded sites ship._

| Skill | Source | What it does |
|---|---|---|
| [`burpsuite-project-parser`](vendored/trailofbits/plugins/burpsuite-project-parser/skills/burpsuite-project-parser/SKILL.md) | trailofbits | Searches and explores Burp Suite project files (.burp) from the command line. Use when searching response headers or bodies with regex patterns, extracting secu |
| [`testing-apis`](vendored/trilwu/secskills-offense/skills/testing-apis/SKILL.md) | trilwu | Test REST and GraphQL APIs for authentication bypasses, authorization flaws, IDOR, mass assignment, injection attacks, and rate limiting issues. Use when pentes |
| [`testing-web-applications`](vendored/trilwu/secskills-offense/skills/testing-web-applications/SKILL.md) | trilwu | Test web applications for security vulnerabilities including SQLi, XSS, command injection, JWT attacks, SSRF, file uploads, XXE, and API flaws. Use when pentest |

### Governance, risk & compliance

_Risk scoring, control mapping (NIST/ISO/SOC2), findings reporting._

| Skill | Source | What it does |
|---|---|---|
| [`GRC & Compliance`](vendored/masriyan/skills/19-grc-compliance/SKILL.md) | masriyan | Governance, risk, and compliance — risk assessment and scoring, control mapping across NIST CSF 2.0 / ISO 27001:2022 / SOC 2 / CIS Controls v8, gap analysis, au |
| [`reporting-security-findings`](vendored/trilwu/secskills-core/skills/reporting-security-findings/SKILL.md) | trilwu | Write security findings and assessment reports — severity scoring with CVSS and business impact, reproducible proof of concept, remediation guidance, executive  |

### Meta & workflow tooling

_Skill authoring, devcontainers, gh CLI, second opinions, open-sourcing._

| Skill | Source | What it does |
|---|---|---|
| [`authoring-security-skills`](vendored/trilwu/.claude/skills/authoring-security-skills/SKILL.md) | trilwu | Write a new SecSkills skill end to end — choosing the plugin bucket and skill tier, writing a description that triggers correctly without stealing traffic from  |
| [`chrome-mcp-troubleshooting`](vendored/trailofbits/plugins/claude-in-chrome-troubleshooting/skills/chrome-mcp-troubleshooting/SKILL.md) | trailofbits | Diagnose and fix Claude in Chrome MCP extension connectivity issues. Use when mcp__claude-in-chrome__* tools fail, return "Browser extension is not connected",  |
| [`code-improver`](vendored/trailofbits/plugins/code-improver/skills/code-improver/SKILL.md) | trailofbits | Runs an autonomous review-and-fix improvement loop over any code target — a skill, plugin, module, or directory — using a reviewer the user names: any installed |
| [`gh-cli`](vendored/trailofbits/plugins/gh-cli/skills/gh-cli/SKILL.md) | trailofbits | Enforces authenticated gh CLI workflows over unauthenticated curl, WebFetch, and MCP fetch patterns. Use when working with GitHub URLs, API access, pull request |
| [`github-triage`](vendored/trailofbits/plugins/github-triage/skills/github-triage/SKILL.md) | trailofbits | Triages a repository's open GitHub issues and pull requests via the gh CLI. Optionally reviews and merges ready PRs — incrementally merging passing automated/bo |
| [`open-sourcing`](vendored/trailofbits/plugins/open-sourcing/skills/open-sourcing/SKILL.md) | trailofbits | This skill should be used when the user asks to "open source this project", "prepare this repository for public release", "make this repo public", "check open-s |
| [`pr-improver`](vendored/trailofbits/plugins/code-improver/skills/pr-improver/SKILL.md) | trailofbits | Runs an autonomous review-and-fix improvement loop over the current branch's changes until a PR review comes back clean, scoped mechanically to the directories  |
| [`second-opinion`](vendored/trailofbits/plugins/second-opinion/skills/second-opinion/SKILL.md) | trailofbits | Runs external LLM code reviews (OpenAI Codex or Google Antigravity CLI) on uncommitted changes, branch diffs, or specific commits. Use when the user asks for a  |
| [`skill-improver`](vendored/trailofbits/plugins/code-improver/skills/skill-improver/SKILL.md) | trailofbits | Runs an autonomous review-and-fix improvement loop over a Claude Code skill until a review comes back clean, with a cross-round findings ledger, escalation when |
| [`testing-handbook-generator`](vendored/trailofbits/plugins/testing-handbook-skills/skills/testing-handbook-generator/SKILL.md) | trailofbits | Generates Claude Code skills from the Trail of Bits Testing Handbook (appsec.guide), analyzing handbook pages and emitting SKILL.md files with the structure eac |
| [`verifying-skill-accuracy`](vendored/trilwu/.claude/skills/verifying-skill-accuracy/SKILL.md) | trilwu | Fact-check LLM-drafted technical content against primary sources — source hierarchy, programmatic existence probes for tool and plugin names, class-before-insta |

### Offensive / penetration testing (authorized only)

_Red-team tradecraft. Only against systems you are explicitly authorized to test._

| Skill | Source | What it does |
|---|---|---|
| [`OT / ICS / SCADA Security`](vendored/masriyan/skills/18-ot-ics-security/SKILL.md) | masriyan | Operational Technology and industrial control system security — Purdue model segmentation, industrial protocol analysis (Modbus, DNP3, S7, EtherNet/IP), PLC/HMI |
| [`Reconnaissance & OSINT Automation`](vendored/masriyan/skills/01-recon-osint/SKILL.md) | masriyan | Passive and active reconnaissance, subdomain enumeration, DNS analysis, technology fingerprinting, and OSINT data correlation for authorized security assessment |
| [`Red Team Operations & Engagement Planning`](vendored/masriyan/skills/14-red-team-ops/SKILL.md) | masriyan | Authorized red team engagement planning, C2 architecture design, attack methodology, lateral movement strategy, OPSEC, and professional reporting |
| [`abusing-adcs`](vendored/trilwu/secskills-offense/skills/abusing-adcs/SKILL.md) | trilwu | Enumerate and abuse Active Directory Certificate Services with Certipy and Certify — the ESC1 through ESC16 escalation paths, vulnerable template and CA configu |
| [`abusing-ci-cd-oidc`](vendored/trilwu/secskills-offense/skills/abusing-ci-cd-oidc/SKILL.md) | trilwu | Exploit CI/CD pipeline misconfigurations and OIDC federation weaknesses across GitHub Actions, GitLab CI, and Jenkins -- poisoned workflows, secret exfiltration |
| [`attacking-active-directory`](vendored/trilwu/secskills-offense/skills/attacking-active-directory/SKILL.md) | trilwu | Attack and enumerate Active Directory environments using Kerberos attacks (Kerberoasting, ASREPRoasting), credential dumping (DCSync, Mimikatz), lateral movemen |
| [`attacking-bluetooth-nfc`](vendored/trilwu/secskills-offense/skills/attacking-bluetooth-nfc/SKILL.md) | trilwu | Attack Bluetooth Classic, BLE, and NFC targets -- device enumeration, GATT characteristic exploitation, BLE MITM and replay, Ubertooth and nRF sniffing, MIFARE  |
| [`attacking-eks-gke-aks`](vendored/trilwu/secskills-offense/skills/attacking-eks-gke-aks/SKILL.md) | trilwu | Assess managed Kubernetes clusters on EKS, GKE, and AKS by exploiting the seams between cloud IAM and Kubernetes RBAC -- IRSA/OIDC trust abuse, Workload Identit |
| [`attacking-entra-id`](vendored/trilwu/secskills-offense/skills/attacking-entra-id/SKILL.md) | trilwu | Attack and enumerate Azure AD / Entra ID tenants — initial recon with AADInternals and ROADtools, password spraying, token theft (PRT, CAE, refresh tokens), app |
| [`attacking-graphql`](vendored/trilwu/secskills-offense/skills/attacking-graphql/SKILL.md) | trilwu | Test GraphQL APIs — introspection and schema recovery when introspection is disabled, field suggestion abuse, batching and alias-based rate limit bypass, query  |
| [`attacking-grpc-protobuf`](vendored/trilwu/secskills-offense/skills/attacking-grpc-protobuf/SKILL.md) | trilwu | Test gRPC and Protocol Buffers services — recovering .proto definitions from server reflection or compiled descriptors, calling methods with grpcurl and grpcui, |
| [`attacking-hardware-interfaces`](vendored/trilwu/secskills-offense/skills/attacking-hardware-interfaces/SKILL.md) | trilwu | Assess the physical attack surface of embedded devices — finding and using UART consoles, JTAG/SWD debug, and SPI/I2C flash; dumping firmware off-chip; triaging |
| [`attacking-jwt`](vendored/trilwu/secskills-offense/skills/attacking-jwt/SKILL.md) | trilwu | Attack JSON Web Tokens by breaking the server's signature-verification decision — alg:none and its case variants, RS256-to-HS256 key confusion using the public  |
| [`attacking-kerberos-delegation`](vendored/trilwu/secskills-offense/skills/attacking-kerberos-delegation/SKILL.md) | trilwu | Identify and abuse Active Directory Kerberos delegation — unconstrained delegation with printer-bug coercion, constrained delegation with protocol transition (S |
| [`attacking-oauth-oidc`](vendored/trilwu/secskills-offense/skills/attacking-oauth-oidc/SKILL.md) | trilwu | Attack OAuth 2.0 and OpenID Connect flows — enumerate endpoints from the OIDC discovery document, break redirect_uri validation with path traversal, open-redire |
| [`attacking-saml`](vendored/trilwu/secskills-offense/skills/attacking-saml/SKILL.md) | trilwu | Attack SAML single sign-on by decoding and tampering with signed XML assertions — XML signature wrapping (XSW1-XSW8), signature stripping, assertion and attribu |
| [`attacking-serverless`](vendored/trilwu/secskills-offense/skills/attacking-serverless/SKILL.md) | trilwu | Attack serverless compute — AWS Lambda, Azure Functions, GCP Cloud Functions, and edge runtimes like Cloudflare Workers. Enumerate functions, inject through eve |
| [`attacking-wireless-networks`](vendored/trilwu/secskills-offense/skills/attacking-wireless-networks/SKILL.md) | trilwu | Attack WiFi networks using WPA/WPA2 cracking, WPS exploitation, Evil Twin attacks, deauthentication, and wireless reconnaissance. Use when pentesting wireless n |
| [`bypassing-mobile-pinning`](vendored/trilwu/secskills-offense/skills/bypassing-mobile-pinning/SKILL.md) | trilwu | Diagnose and defeat TLS interception failures in mobile apps — certificate pinning, Android Network Security Config, user-CA distrust, native BoringSSL pinning, |
| [`bypassing-root-jailbreak-detection`](vendored/trilwu/secskills-offense/skills/bypassing-root-jailbreak-detection/SKILL.md) | trilwu | Defeat root, jailbreak, emulator, debugger, and Frida detection in mobile apps using Magisk DenyList, Zygisk modules, objection, and targeted Frida hooks, and u |
| [`cracking-passwords`](vendored/trilwu/secskills-offense/skills/cracking-passwords/SKILL.md) | trilwu | Crack password hashes using hashcat/john, perform password spraying, brute force authentication, and execute pass-the-hash attacks. Use when cracking credential |
| [`enumerating-network-services`](vendored/trilwu/secskills-offense/skills/enumerating-network-services/SKILL.md) | trilwu | Enumerate and exploit network services including SMB, FTP, SSH, RDP, HTTP, databases (MySQL, MSSQL, PostgreSQL, MongoDB), LDAP, NFS, DNS, and SNMP. Use when tes |
| [`escalating-linux-privileges`](vendored/trilwu/secskills-offense/skills/escalating-linux-privileges/SKILL.md) | trilwu | Escalate privileges on Linux systems using SUID/SGID binaries, capabilities, sudo misconfigurations, cron jobs, kernel exploits, and container escapes. Use when |
| [`escalating-windows-privileges`](vendored/trilwu/secskills-offense/skills/escalating-windows-privileges/SKILL.md) | trilwu | Escalate privileges on Windows systems using service misconfigurations, DLL hijacking, token manipulation, UAC bypasses, registry exploits, and credential dumpi |
| [`escaping-hardened-containers`](vendored/trilwu/secskills-offense/skills/escaping-hardened-containers/SKILL.md) | trilwu | Escape containers that drop capabilities, enforce seccomp profiles, and run behind AppArmor or SELinux — enumerating residual capabilities, analyzing seccomp fi |
| [`establishing-persistence`](vendored/trilwu/secskills-offense/skills/establishing-persistence/SKILL.md) | trilwu | Establish persistence on Windows and Linux systems using registry keys, scheduled tasks, services, cron jobs, SSH keys, backdoor accounts, and rootkits. Use whe |
| [`exploiting-cloud-platforms`](vendored/trilwu/secskills-offense/skills/exploiting-cloud-platforms/SKILL.md) | trilwu | Exploit AWS, Azure, and GCP cloud misconfigurations including S3 buckets, IAM roles, metadata services, serverless functions, and cloud-specific privilege escal |
| [`exploiting-containers`](vendored/trilwu/secskills-offense/skills/exploiting-containers/SKILL.md) | trilwu | Escape Docker containers and exploit Kubernetes clusters using privileged containers, Docker socket access, misconfigurations, and API abuse. Use when testing c |
| [`exploiting-deserialization`](vendored/trilwu/secskills-offense/skills/exploiting-deserialization/SKILL.md) | trilwu | Identify and exploit insecure deserialization across Java, .NET, PHP, Python, and Ruby — recognizing serialized formats by magic bytes, finding gadget chains wi |
| [`exploiting-memory-corruption`](vendored/trilwu/secskills-offense/skills/exploiting-memory-corruption/SKILL.md) | trilwu | Develop working exploits from memory-corruption bugs in native binaries — turning a stack/heap overflow, use-after-free, or type confusion into control flow, an |
| [`exploiting-ssrf`](vendored/trilwu/secskills-offense/skills/exploiting-ssrf/SKILL.md) | trilwu | Find and exploit server-side request forgery — reaching cloud instance metadata on AWS IMDSv1/IMDSv2, Azure IMDS, and GCP, internal service discovery, filter an |
| [`exploiting-web3-smart-contracts`](vendored/trilwu/secskills-offense/skills/exploiting-web3-smart-contracts/SKILL.md) | trilwu | Audit and exploit smart contracts and Web3 applications including reentrancy, integer overflow, access control flaws, and DeFi-specific vulnerabilities. Use whe |
| [`exploiting-xxe`](vendored/trilwu/secskills-offense/skills/exploiting-xxe/SKILL.md) | trilwu | Exploit XML External Entity injection to read local files and reach internal services — in-band file read, php://filter base64 wrappers, SSRF to cloud metadata, |
| [`maintaining-engagement-state`](vendored/trilwu/secskills-core/skills/maintaining-engagement-state/SKILL.md) | trilwu | Keep the durable record that outlives a session — credential provenance, access inventory, artifacts left on target for cleanup, findings with evidence, and a d |
| [`orchestrating-vulnerability-research`](vendored/trilwu/secskills-core/skills/orchestrating-vulnerability-research/SKILL.md) | trilwu | Run a sustained, multi-agent vulnerability-discovery campaign against a target — split its attack surface into slices, hunt each slice with a builder agent, and |
| [`performing-reconnaissance`](vendored/trilwu/secskills-offense/skills/performing-reconnaissance/SKILL.md) | trilwu | Perform OSINT, subdomain enumeration, port scanning, web reconnaissance, email harvesting, and cloud asset discovery for initial access. Use when gathering inte |
| [`performing-social-engineering`](vendored/trilwu/secskills-offense/skills/performing-social-engineering/SKILL.md) | trilwu | Conduct phishing campaigns, credential harvesting, pretexting, and social engineering attacks using tools like Gophish, SET, and custom techniques. Use when per |
| [`recognizing-deception`](vendored/trilwu/secskills-offense/skills/recognizing-deception/SKILL.md) | trilwu | Recognize defensive deception during an engagement — honeypots, honeytokens and canary tokens, decoy AD accounts and shares, canary files, and deceptive cloud c |
| [`testing-ics-ot-protocols`](vendored/trilwu/secskills-offense/skills/testing-ics-ot-protocols/SKILL.md) | trilwu | Test Industrial Control Systems and Operational Technology protocols — Modbus, DNP3, OPC UA, BACnet, EtherNet/IP, S7comm, MQTT — with safety-first methodology f |
| [`testing-thick-clients`](vendored/trilwu/secskills-offense/skills/testing-thick-clients/SKILL.md) | trilwu | Security-test desktop thick-client applications (.NET/WPF, Java, Electron, native Win32) against their local and network attack surface — proxying non-HTTP traf |
| [`transferring-files`](vendored/trilwu/secskills-offense/skills/transferring-files/SKILL.md) | trilwu | Transfer files between systems using HTTP, SMB, FTP, netcat, base64 encoding, and living-off-the-land techniques for both Linux and Windows. Use when moving too |

## Licensing & attribution

This is an **aggregation**. Copyright stays with the original authors and each skill remains under its upstream license:

- **trailofbits/skills** — CC-BY-SA-4.0 ([license](LICENSES/trailofbits-CC-BY-SA-4.0.txt))
- **Masriyan/Claude-Code-CyberSecurity-Skill** — MIT ([license](LICENSES/masriyan-MIT.txt))
- **trilwu/secskills** — MIT ([license](LICENSES/trilwu-MIT.txt))

Trail of Bits' skills are **CC-BY-SA-4.0**: they are redistributed here with attribution and a link to the license; any modified versions must stay under CC-BY-SA-4.0. The only change made to upstream content is **relocation** into `vendored/` — skill contents are unmodified. See `NOTICE.md`.

## Rebuilding

`README.md`, `catalog.json`, and `.claude-plugin/marketplace.json` are generated. Edit `categories.yaml` (curation) or bump a SHA in `sources.yaml` and re-vendor, then run:

```bash
python scripts/sync.py
```
