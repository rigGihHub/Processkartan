from pathlib import Path
SRC=Path('app.py').read_text(encoding='utf-8')

def test_version():
    assert 'APP_VERSION = "0.20.80"' in SRC

def test_neutral_sidebar_hides_unused_inspector():
    assert '#pk48:not(.p48-side-context-active) #p48-format-panel{display:none!important}' in SRC

def test_secondary_palette_is_collapsible():
    assert 'id="p48-palette-more"' in SRC
    assert 'Start, beslut, dokument…' in SRC
    assert 'class="p48-palette-more-grid"' in SRC

def test_core_palette_remains_directly_available():
    assert 'aria-label="Lägg till Objekt in"' in SRC
    assert 'aria-label="Lägg till Aktivitet"' in SRC
    assert 'aria-label="Lägg till Objekt ut"' in SRC
