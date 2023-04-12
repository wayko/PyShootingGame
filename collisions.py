def detect_collisions(player, bullets, enemies, explosion_sound):
    # Check for collisions between bullets and enemies
    for bullet in bullets:
        for enemy in enemies:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                explosion_sound.play()
                return True

    # Check for collisions between player and enemies
    for enemy in enemies:
        if player.colliderect(enemy):
            return True

    return False
