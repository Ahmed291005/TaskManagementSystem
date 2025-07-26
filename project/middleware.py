from django.shortcuts import render

class RestrictAdminMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Restrict admin panel access
        if request.path.startswith("/admin/"):
            user = getattr(request, "user", None)
            if not user or not user.is_authenticated or not user.is_staff:
                return render(request, "account/403.html", status=403)
                
        return self.get_response(request)
