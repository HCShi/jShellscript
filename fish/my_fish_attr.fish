# Use Sapce or Enter
if status --is-interactive
    set -g fish_user_abbreviations
    abbr --add first 'echo my first abbreviation'
    abbr --add second 'echo my second abbreviation'
end
