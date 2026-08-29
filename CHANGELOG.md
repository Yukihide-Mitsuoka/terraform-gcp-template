# Changelog

## [1.4.4](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/compare/v1.4.3...v1.4.4) (2026-08-29)


### Bug Fixes

* **ci:** skip public-only security jobs in private repos ([#160](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/160)) ([f923e02](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/f923e022b7d57c0bc2b6e5595dc9aa3979d16b66))

## [1.4.3](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/compare/v1.4.2...v1.4.3) (2026-08-14)


### Bug Fixes

* upgrade protected workflow actions ([#154](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/154)) ([c459146](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/c45914668487b184935410bdb4d9d8ec0263dafe)), closes [#153](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/153)

## [1.4.2](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/compare/v1.4.1...v1.4.2) (2026-08-09)


### Bug Fixes

* **sync:** prevent duplicate template reviews ([#149](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/149)) ([415922a](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/415922a40db48ae6e2500bf54f66c62a52847d78))

## [1.4.1](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/compare/v1.4.0...v1.4.1) (2026-08-09)


### Bug Fixes

* **ci:** upgrade CodeQL Action to v4 ([#146](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/146)) ([58a349e](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/58a349ed2210950e971a716ffec12627ceecd77b))
* **inheritance:** migrate Template Sync instructions ([#144](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/144)) ([76063e6](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/76063e6772c5b6178c516f8365c7ed9722b0c52a))

## [1.4.0](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/compare/v1.3.3...v1.4.0) (2026-08-08)


### Features

* **inheritance:** publish Terraform child export ([#137](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/137)) ([e510105](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/e510105629c8eea4ee1c82cbcf3a63134a6a1746))


### Bug Fixes

* **inheritance:** make seed tests child-portable ([#141](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/141)) ([d011aca](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/d011aca625f0e49d612ee718b554ccbaa5d9f422))

## [1.3.3](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/compare/v1.3.2...v1.3.3) (2026-08-02)


### Bug Fixes

* **release:** restore stack prerequisites ([#130](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/130)) ([85873ed](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/85873ed59c522f418c10e90844d6b487f7fdbbd8)), closes [#129](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/129)

## [1.3.2](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/compare/v1.3.1...v1.3.2) (2026-08-02)


### Bug Fixes

* **ci:** call Scorecard directly ([#122](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/122)) ([340752b](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/340752b3ffffcd561e71bc92b0c401d37d903a13)), closes [#121](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/121)
* **release:** attach SBOM to created release ([#128](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/128)) ([77ddd5b](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/77ddd5bbffa62cf07108a81fe44f403fb73e5462)), closes [#127](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/127)

## [1.3.1](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/compare/v1.3.0...v1.3.1) (2026-08-01)


### Bug Fixes

* **ci:** authenticate oversized template syncs ([#111](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/111)) ([85906c1](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/85906c10cff49b4f18b1719e88b808aa62d687d3)), closes [#110](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/110)
* **ci:** isolate project size policy ([#115](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/115)) ([ca1e08d](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/ca1e08d14a0c34339f75d423eed357961705be0d)), closes [#114](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/114)

## [1.3.0](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/compare/v1.2.0...v1.3.0) (2026-08-01)


### Features

* **inheritance:** export Terraform template overlay ([#103](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/103)) ([331a724](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/331a724dc112f9390c3f2d3322394cb6cd133984))


### Bug Fixes

* **inheritance:** inherit foundation bugfix skill ([#107](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/107)) ([6864b33](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/6864b33889da80122f6dab4e4c5ebd5f2433007a))

## [1.2.0](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/compare/v1.1.0...v1.2.0) (2026-07-30)


### Features

* **inheritance:** prove manifest v2 agent profile ([#90](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/90)) ([1c13ce6](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/1c13ce6fe8609531816a8f86e8cfcbdb9e4bac0f))

## [1.1.0](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/compare/v1.0.0...v1.1.0) (2026-07-29)


### Features

* **ai:** add context budget engine ([#82](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/82)) ([93a48f4](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/93a48f40e80d2fe24e14d65bdf84929f20626f65))
* **ai:** audit root README ownership ([#80](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/80)) ([cb7d835](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/cb7d8358e7e283399d0d27ece8511505aa3b08be))
* **ai:** enforce context budget contract ([#83](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/83)) ([92df8d5](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/92df8d55aecded9216226a7b3079030fac1dc0b9))

## 1.0.0 (2026-07-28)


### ⚠ BREAKING CHANGES

* **governance:** scripts/setup-github.sh now requires an explicit OWNER/REPOSITORY target; apply also requires the same target after --confirm-repo.

### Features

* **governance:** add inherited policy validation ([0b623e0](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/0b623e0f35f31e6ccd9d0c76e1434c52e2e38b37))
* **governance:** add inherited policy validation ([c220491](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/c220491389695164b749db76e849b9c3b3b14711)), closes [#2](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/2)
* **governance:** add Terraform profile ([6763ef4](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/6763ef4ed0232038b684820744241d8e9807f5aa))
* **governance:** add Terraform profile ([52fbbe2](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/52fbbe2efe4520a396f83479247151ad6beaa27a)), closes [#2](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/2)
* **governance:** add verified apply execution boundary ([75dfd6c](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/75dfd6cc21fe4f3ed3988d1ded5a977d8c48d8f7))
* **governance:** add verified apply execution boundary ([1c354b4](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/1c354b4ef895a5c7b0b26516c7dd0315f9c2d5bf)), closes [#2](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/2)
* **governance:** enforce vulnerability intake controls ([10e4a1a](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/10e4a1a13f0cd7db973e986f7aafb8e5a5fb0174))
* **governance:** enforce vulnerability intake controls ([2d56842](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/2d56842f7e9d93d5dd543a451cba4ae7f5f72506)), closes [#2](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/2)
* **governance:** expose confirmed apply command ([d8fc759](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/d8fc759220007751d534f7d50f917db4c89f08cd))
* **governance:** expose confirmed apply command ([8db69b3](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/8db69b3a643ecb7a781150f4bd2b255b2c850c58)), closes [#2](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/2)
* **governance:** inherit apply action planning ([edd5698](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/edd5698f291f47aaba0f7c99f6b10327072f3ca7))
* **governance:** inherit apply action planning ([fb73952](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/fb73952e847689bd72844325585342f19bfe81cd))
* **governance:** inherit collaboration settings ([414aa03](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/414aa03c69b8f16a096a6cc860a2a3e3a4469a46))
* **governance:** inherit collaboration settings ([52b355c](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/52b355ca356f6b11d274a30aab153c92520d315d)), closes [#2](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/2)
* **governance:** inherit deterministic comparison ([40a63a1](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/40a63a15ff71a72402a32e9391a8b86811e8ceb8))
* **governance:** inherit deterministic comparison ([e9bd0f7](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/e9bd0f7452b6d439e600d4365991d26c61a2da1a))
* **governance:** inherit plan and audit commands ([5ced34f](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/5ced34ffbcac664d77a552d02a79a0c29c49eddb))
* **governance:** inherit plan and audit commands ([743e457](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/743e457bc28bb7b3c9276af9cbff527718522cf4))
* **governance:** inherit read-only GitHub discovery ([5324852](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/532485212674dd29fc3943659bac9802893b60eb))
* **governance:** inherit read-only GitHub discovery ([61a56d0](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/61a56d0ba1341daf64b381696bc194ce713c9ee6))
* **governance:** inherit setup policy wrapper ([c42d55a](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/c42d55a879e4a089cfd0d302906134affff236ff)), closes [#2](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/2)
* **governance:** inherit solo-friendly defaults ([8e5829c](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/8e5829c47e2f179243f5922259d1d95bf3b0c3ae))
* **governance:** inherit solo-friendly defaults ([205d877](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/205d877f02964f53dcf0a7d8a1721eb4f848231b))
* **governance:** inherit template profile chain ([d789acc](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/d789accc55d71e69ae0d668efa069b9ef956a320))
* **governance:** inherit template profile chain ([dbc6880](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/dbc6880960cf20dc30261a9e8445d2ae0e7db61d)), closes [#2](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/2)
* **governance:** preserve stricter ruleset constraints ([90bdc90](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/90bdc904d512d6cadf7efb085a726fca6c6026ef))
* **governance:** preserve stricter ruleset constraints ([3d2fc36](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/3d2fc36eb0b303e6b2f024c3092fd3e041487bb4))
* **inheritance:** bootstrap contract validator ([5188aad](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/5188aad0add15c80233a21b5fd6ae7d15aec2875))
* **inheritance:** bootstrap contract validator ([0a7f7ee](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/0a7f7eef8cbd269d310d46bebef9cc2c745fe414))
* **inheritance:** bootstrap direct-parent contract ([04242f6](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/04242f6e2ef55104fc8c063186e1565fdb2d28e0))
* **inheritance:** bootstrap direct-parent contract ([31cb2c5](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/31cb2c524f1ff522a7a2104c3645f5201ee50c5f)), closes [#2](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/2)
* **inheritance:** bootstrap read-only planner ([48d3f38](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/48d3f38f86a800d622b8a4352c9e6f06c98495f9))
* **inheritance:** bootstrap read-only planner ([0736ac4](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/0736ac460edf951395baf38e627fb9f55049674c))
* instantiate GCP Terraform starter on the ai-dev-foundation base ([f439b44](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/f439b44f8219c75771c2f41f33a5c0c2d887b06f))


### Bug Fixes

* **ci:** install terraform in lint/build jobs (runners do not ship it) ([157b3c2](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/157b3c2e299722f35957c15e915139aa64730fe1))
* **governance:** adopt ruleset-only discovery ([#57](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/57)) ([de7df1b](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/de7df1b760534644eb97b9bdd10ab72adb5f665c))
* **infra:** pin flow-log-enabled network module ([#54](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/54)) ([bf70f53](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/bf70f53ee682d4614cceea6b3dae86dfaf01a6d4))
* make setup resilient when pre-commit is absent (CI runners) ([148d09d](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/148d09d7787b5410fc14c863947b15104a978606))
* **security:** configure CodeQL language matrix ([#61](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/61)) ([5ecd560](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/5ecd5605a8c1adf082bd82195de73f79c1bc4611))
* **sync:** adopt safe parent propagation ([#55](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/55)) ([beb5310](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/beb5310db975811a3da0b37bbf6ad8837d9e31b7))
* **sync:** keep PR body inside workflow script ([#59](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/59)) ([b617042](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/b617042dcd129abc016c7a0e13e8adcb51a341cf))
* **sync:** run child contract validation ([#56](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/56)) ([5a838b0](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/5a838b0b8c32f2d6b0be9fa2f8a47f22450ea683))
* **template-sync:** allow foundation docs ([#38](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/issues/38)) ([7b9dfe7](https://github.com/Yukihide-Mitsuoka/terraform-gcp-template/commit/7b9dfe7cd5cbcb82243dcac340a16f29c559c9ac))
