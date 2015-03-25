import classes
game=classes.game()
game.CreatePlayer(classes.player("hubert"))
game.CreateHero(classes.hero("hans","fire"))
game.CreateEnemy(classes.enemy(1,"fire"))
while(1):
    game.PrintStatus()
    m_input=raw_input()
    if (m_input=="1"):
        game.Attack()
    if (m_input=="2"):
        game.Upgrade()
    if (m_input=="3"):
        game.Regenerate()
    if (m_input=="4"):
        break
            
                
        
