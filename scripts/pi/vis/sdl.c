#include <stdio.h>
#include <SDL.h>

#define WIDTH  500
#define HEIGHT 500

void
printInfo(void) 
{
  int secs, pct;
  SDL_version compiled;
  SDL_version linked;

  SDL_VERSION(&compiled);
  SDL_GetVersion(&linked);

  printf("We compiled against SDL version %d.%d.%d ...\n", compiled.major, compiled.minor, compiled.patch);
  printf("But we are linking against SDL version %d.%d.%d.\n", linked.major, linked.minor, linked.patch);
  printf("%s\n", SDL_GetPlatform());
  printf("3D Now: %d, Altivec: %d, AVX2: %d, MMX: %d, RDTSC: %d, SSE: %d, SSE2: %d, SSE3: %d, SSE41: %d, SSE42l %d\n", SDL_Has3DNow(), SDL_HasAltiVec(), SDL_HasAVX2(), SDL_HasMMX(), SDL_HasRDTSC(), SDL_HasSSE(), SDL_HasSSE2(), SDL_HasSSE3(), SDL_HasSSE41(), SDL_HasSSE42());

  if (SDL_GetPowerInfo(&secs, &pct) != SDL_POWERSTATE_UNKNOWN) {
    printf("Battery is draining: ");
    if (secs == -1) {
        printf("(unknown time left)\n");
    } else {
        printf("(%d seconds left)\n", secs);
    }

    if (pct == -1) {
        printf("(unknown percentage left)\n");
    } else {
        printf("(%d percent left)\n", pct);
    }
  }
}

int 
main(int argc, char* argv[])
{

  if (SDL_Init(SDL_INIT_VIDEO) == 0) {

    SDL_Window* window = NULL;
    SDL_Renderer* renderer = NULL;

    if (SDL_CreateWindowAndRenderer(WIDTH, HEIGHT, 0, &window, &renderer) == 0) {

      SDL_SetWindowTitle(window, "ZapOztasi");
      SDL_bool done = SDL_FALSE;

      int x = 0;

      while (!done) {
        SDL_Event event;

        double r = fmodl(drand48(), 0.8) + 0.1;
        double g = fmodl(drand48(), 0.8) + 0.1;
        double b = fmodl(drand48(), 0.8) + 0.1;
        double a = fmodl(drand48(), 0.8) + 0.1;

        SDL_SetRenderDrawColor(renderer, 0, 0, 255 * b, 255);
        SDL_Rect rectangle;

        rectangle.x = x++;
        rectangle.y = 0;
        rectangle.w = 1;
        rectangle.h = HEIGHT;

        SDL_RenderFillRect(renderer, &rectangle);
        SDL_RenderPresent(renderer);

        if (x == WIDTH) {
          x ^= x;
          SDL_SetRenderDrawColor(renderer, 0, 0, 0, SDL_ALPHA_OPAQUE);
          SDL_RenderClear(renderer);
        }

        SDL_Delay(10);

        while (SDL_PollEvent(&event)) {
          if (event.type == SDL_QUIT) {
            done = SDL_TRUE;
          }
        }
      }
    }

    if (renderer) {
      SDL_DestroyRenderer(renderer);
    }
    if (window) {
      SDL_DestroyWindow(window);
    }
  }

  SDL_Quit();

  return 0;
}
