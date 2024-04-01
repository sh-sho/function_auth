# OCI Vault Hands-on

* 前提条件
* ハンズオン全体像
* 事前準備
* OCI Vaultのハンズオン
    * OCI Vaultの作成
        * Master Encryption Keysの作成
        * Secretの作成
    * OCI Functionsの作成
        * アプリケーションの作成
        * コンテキストの更新
        * Function コードの説明
        * Functionのデプロイ
        * Functionを用いてSecretを取得


## 前提条件
* Compute, OCI Functions を実行するために必要なポリシーや仮想ネットワーク(VCN)が作成済みであること
* Cloud Shell が使用可能な環境であること
    * 未実施の場合は、[Oracle Cloud Infrastructure ドキュメント - クラウド・シェル](#https://docs.oracle.com/ja-jp/iaas/Content/API/Concepts/cloudshellintro.htm)を参考に、必要なポリシー等を設定してください
    * Cloud Shell/OCI Functions の CPU アーキテクチャは、X86 で統一すること
* 各種ツール、言語、ライブラリのバージョンは、Cloud Shell に事前にインストールされているものに従います
    * OCI CLI: 3.38.0
    * Fn Project: 0.6.29
    * Python: 3.8.13
    * SDK for Python: 2.125.0

## ハンズオン全体像

## 事前準備
### ハンズオンで使うコードのクローン
ハンズオンを実施するにあたり、本リポジトリを Cloud Shell 上にクローンします。



## OCI Vaultのハンズオン
### OCI Vaultの作成
#### Master Encryption Keysの作成
#### Secretの作成
### OCI Functionsの作成
#### アプリケーションの作成
#### コンテキストの更新
#### Function コードの説明
#### Functionのデプロイ
#### FunctionのConfigurationの設定
#### Functionを用いてSecretを取得
