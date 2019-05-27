import test_package
import test_package.menu

test_package.menu.show_menu()

import test_package.games.contra
from test_package.games.tanks import play
from test_package.games import supermario

test_package.games.contra.play()
play()#tanks
test_package.games.supermario.play()