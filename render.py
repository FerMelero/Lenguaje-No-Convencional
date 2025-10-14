import pygame

pygame.init()
pygame.font.init()

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY  = (200, 200, 200)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)

# Ventana
size = width, height = 1000, 800
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
font = pygame.font.SysFont("DejaVu Sans", 20)
bigfont = pygame.font.SysFont("DejaVu Sans", 26)


def get_reg_list_for_ui(regs_dict):
    ordered = [regs_dict.get("$aux", 0), regs_dict.get("$res", 0)]
    for name in ["$t2", "$t3", "$t4", "$t5", "$t6", "$t7", "$t8", "$t9", "$t10"]:
        ordered.append(regs_dict.get(name, 0))
    return ordered

def render_registros(interp):
    regs = get_reg_list_for_ui(interp.registros)
    for x in range(11):
        rect_x = 15 + 80 * x
        rect_y = 60
        pygame.draw.rect(screen, BLACK, pygame.Rect(rect_x, rect_y, 70, 70), width=2)

        label_text = "aux" if x == 0 else "res" if x == 1 else f"{x}♣"
        label_surface = font.render(label_text, True, BLACK)
        label_rect = label_surface.get_rect(center=(rect_x + 35, rect_y - 14))
        screen.blit(label_surface, label_rect)

        value = regs[x] if x < len(regs) else 0
        value_surface = bigfont.render(str(value), True, BLACK)
        value_rect = value_surface.get_rect(center=(rect_x + 35, rect_y + 35))
        screen.blit(value_surface, value_rect)

def render_instruccion(interp):
    # Caja más pequeña y más arriba
    instr_box = pygame.Rect(350, 150, 600, 90)
    pygame.draw.rect(screen, BLACK, instr_box, width=2)
    label = font.render("Instrucción actual", True, BLACK)
    screen.blit(label, (instr_box.x + 10, instr_box.y - 25))

    instr_surface = bigfont.render(interp.current_instruction_str(), True, BLACK)
    screen.blit(instr_surface, (instr_box.x + 10, instr_box.y + 10))

    # Mostrar siguientes instrucciones (más cerca)
    ctx_y = instr_box.y + instr_box.h + 8
    for offset in range(1, 5):  # menos líneas para que no se monte
        idx = interp.i + offset
        if 0 <= idx < len(interp.palabras):
            text = f"{idx:03d}: " + " ".join(interp.palabras[idx])
            surf = font.render(text, True, BLACK)
            screen.blit(surf, (instr_box.x + 10, ctx_y))
            ctx_y += 22

def render_consola(interp):
    cons = pygame.Rect(350, 380, 600, 330)
    pygame.draw.rect(screen, BLACK, cons, width=2)
    label = font.render("Salida", True, BLACK)
    screen.blit(label, (cons.x + 10, cons.y - 25))
    y = cons.y + 10
    for line in interp.output_lines[-10:]:
        surf = font.render(str(line), True, BLACK)
        screen.blit(surf, (cons.x + 10, y))
        y += 22

def render_botones():
    # Subimos los botones (antes 520 → ahora ~360)
    btn_x, btn_y, btn_w, btn_h, gap = 15, 150, 240, 40, 8
    buttons = ["STEP (SPACE)", "RESET (R)", "QUIT (ESC)"]

    for i, text in enumerate(buttons):
        r = pygame.Rect(btn_x, btn_y + i * (btn_h + gap), btn_w, btn_h)
        pygame.draw.rect(screen, GRAY, r)
        pygame.draw.rect(screen, BLACK, r, width=2)
        t = font.render(text, True, BLACK)
        screen.blit(t, t.get_rect(center=r.center))
