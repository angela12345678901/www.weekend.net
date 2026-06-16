import re

class MessageProcessor:
    def __init__(self, max_repeats=3):
        self.max_repeats = max_repeats
        self.assistant_history = set()
        self.repeat_counter = 0
        self.is_blocked = False

    def _normalize_text(self, text: str) -> str:
        """Limpia el texto: minúsculas, quita espacios extra y puntuación."""
        text = text.lower().strip()
        text = re.sub(r'[^\w\s]', '', text)  # Elimina signos de puntuación
        return " ".join(text.split())

    def process_turn(self, user_message: str, pending_response: str) -> dict:
        """
        Procesa el turno actual del chat.
        Devuelve un diccionario con el estado y la acción recomendada.
        """
        if self.is_blocked:
            return {"status": "blocked", "action": "reject", "message": "Processor is locked."}

        norm_user = self._normalize_text(user_message)
        norm_assistant = self._normalize_text(pending_response)

        # Validación: ¿El usuario está copiando al asistente?
        if norm_user in self.assistant_history:
            self.repeat_counter += 1
            if self.repeat_counter >= self.max_repeats:
                self.is_blocked = True
                return {
                    "status": "alert",
                    "action": "block_user",
                    "reason": f"Bucle detectado. Repeticiones: {self.repeat_counter}"
                }
        else:
            # Resetea el contador si el usuario envía algo distinto
            self.repeat_counter = 0

        # Registrar la respuesta aprobada en el historial
        self.assistant_history.add(norm_assistant)

        return {
            "status": "ok",
            "action": "allow",
            "processed_response": pending_response
        }
