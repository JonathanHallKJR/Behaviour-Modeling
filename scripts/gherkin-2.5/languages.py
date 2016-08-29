# -*- coding: utf-8 -*-
# Lettuce - Behaviour Driven Development for python
#
# Copyright (C)  2010-2012  Gabriel Falcão <gabriel@nacaolivre.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Original:
#   https://github.com/gabrielfalcao/lettuce/blob/master/lettuce/languages.py


LANGUAGES = {
    'en': {
        'examples': 'Examples|Scenarios',
        'feature': 'Feature',
        'name': 'English',
        'native': 'English',
        'scenario': 'Scenario',
        'scenario_outline': 'Scenario Outline',
        'scenario_separator': '(Scenario Outline|Scenario)',
        'background': '(?:Background)',
        'given': 'Given',
    },
    'pt-br': {
        'examples': 'Exemplos|Cenários',
        'feature': 'Funcionalidade',
        'name': 'Portuguese',
        'native': 'Português',
        'scenario': 'Cenário|Cenario',
        'scenario_outline': 'Esquema do Cenário|Esquema do Cenario',
        'scenario_separator': '(Esquema do Cenário|Esquema do Cenario|Cenario|Cenário)',
        'background': '(?:Contexto|Considerações)',
    },
    'pl': {
        'examples': 'Przykład',
        'feature': 'Właściwość',
        'name': 'Polish',
        'native': 'Polski',
        'scenario': 'Scenariusz',
        'scenario_outline': 'Zarys Scenariusza',
        'scenario_separator': '(Zarys Scenariusza|Scenariusz)',
        'background': '(?:Background)',
    },
    'ca': {
        'examples': 'Exemples',
        'feature': 'Funcionalitat',
        'name': 'Catalan',
        'native': 'Català',
        'scenario': 'Escenari',
        'scenario_outline': u"Esquema d'Escenari",
        'scenario_separator': u"(Esquema d'Escenari|Escenari)",
        'background': '(?:Background)',
    },
    'es': {
        'examples': 'Ejemplos',
        'feature': 'Funcionalidad',
        'name': 'Spanish',
        'native': 'Español',
        'scenario': 'Escenario',
        'scenario_outline': 'Esquema de Escenario',
        'scenario_separator': '(Esquema de Escenario|Escenario)',
        'background': '(?:Contexto|Consideraciones)',
    },
    'h': {
        'examples': 'Példák',
        'feature': 'Jellemző',
        'name': 'Hungarian',
        'native': 'Magyar',
        'scenario': 'Forgatókönyv',
        'scenario_outline': 'Forgatókönyv vázlat',
        'scenario_separator': '(Forgatókönyv|Forgatókönyv vázlat)',
        'background': '(?:Háttér)',
    },
    'fr': {
        'examples': 'Exemples|Scénarios',
        'feature': 'Fonctionnalité|Fonction',
        'name': 'French',
        'native': 'Français',
        'scenario': 'Scénario',
        'scenario_outline': 'Plan de Scénario|Plan du Scénario',
        'scenario_separator': '(Plan de Scénario|Plan du Scénario|Scénario)',
        'background': '(?:Background|Contexte)',
    },
    'de': {
        'examples': 'Beispiele|Szenarios',
        'feature': 'Funktionalität|Funktion',
        'name': 'German',
        'native': 'Deutsch',
        'scenario': 'Szenario',
        'scenario_outline': 'Szenario-Zusammenfassung|Zusammenfassung',
        'scenario_separator': '(Szenario-Zusammenfassung|Zusammenfassung)',
        'background': '(?:Background)',
    },
    'ja': {
        'examples': '例',
        'feature': 'フィーチャ',
        'name': 'Japanese',
        'native': '日本語',
        'scenario': 'シナリオ',
        'scenario_outline': 'シナリオアウトライン|シナリオテンプレート|テンプレ|シナリオテンプレ',
        'scenario_separator': '(シナリオ|シナリオアウトライン|シナリオテンプレート|テンプレ|シナリオテンプレ)',
        'background': '(?:Background)',
    },
    'tr': {
        'examples': 'Örnekler',
        'feature': 'Özellik',
        'name': 'Turkish',
        'native': 'Türkçe',
        'scenario': 'Senaryo',
        'scenario_outline': 'Senaryo taslağı|Senaryo Taslağı',
        'scenario_separator': '(Senaryo taslağı|Senaryo Taslağı|Senaryo)',
        'background': '(?:Background)',
    },
    'zh-CN': {
        'examples': '例如|场景集',
        'feature': '特性',
        'name': 'Simplified Chinese',
        'native': '简体中文',
        'scenario': '场景',
        'scenario_outline': '场景模板',
        'scenario_separator': '(场景模板|场景)',
        'background': '(?:背景)',
    },
    'zh-TW': {
        'examples': '例如|場景集',
        'feature': '特性',
        'name': 'Traditional Chinese',
        'native': '繁體中文',
        'scenario': '場景',
        'scenario_outline': '場景模板',
        'scenario_separator': '(場景模板|場景)',
        'background': '(?:背景)',
    },
    'r': {
        'examples': 'Примеры|Сценарии',
        'feature': 'Функционал',
        'name': 'Russian',
        'native': 'Русский',
        'scenario': 'Сценарий',
        'scenario_outline': 'Структура сценария',
        'scenario_separator': '(Структура сценария|Сценарий)',
        'background': '(?:Background)',
    },
    'uk': {
        'examples': 'Приклади|Сценарії',
        'feature': 'Функціонал',
        'name': 'Ukrainian',
        'native': 'Українська',
        'scenario': 'Сценарій',
        'scenario_outline': 'Структура сценарію',
        'scenario_separator': '(Структура сценарію|Сценарій)',
        'background': '(?:Background)',
    },
    'it': {
        'examples': 'Esempi|Scenari|Scenarii',
        'feature': 'Funzionalità|Funzione',
        'name': 'Italian',
        'native': 'Italiano',
        'scenario': 'Scenario',
        'scenario_outline': 'Schema di Scenario|Piano di Scenario',
        'scenario_separator': '(Schema di Scenario|Piano di Scenario|Scenario)',
        'background': '(?:Background)',
    },
    'no': {
        'examples': 'Eksempler',
        'feature': 'Egenskaper',
        'name': 'Norwegian',
        'native': 'Norsk',
        'scenario': 'Situasjon',
        'scenario_outline': 'Situasjon Oversikt',
        'scenario_separator': '(Situasjon Oversikt|Situasjon)',
        'background': '(?:Bakgrunn)',
    },
    'sv': {
        'examples': 'Exempel|Scenarion',
        'feature': 'Egenskaper',
        'name': 'Swedish',
        'native': 'Svenska',
        'scenario': 'Scenario',
        'scenario_outline': 'Scenarioöversikt',
        'scenario_separator': '(Scenarioöversikt|Scenario)',
        'background': '(?:Context)',
    },
    'cz': {
        'examples': 'Příklady',
        'feature': 'Požadavek',
        'name': 'Czech',
        'native': 'Čeština',
        'scenario': 'Scénář|Požadavek',
        'scenario_outline': 'Náčrt scénáře',
        'scenario_separator': '(Náčrt scénáře|Scénář)',
        'background': '(?:Background)',
    },
}
