(require 'ox-publish)
(setq org-publish-project-alist
      '(("weather-site-org"
         :base-directory "./content/"
         :base-extension "org"
         :publishing-directory "./public/"
         :recursive t
         :publishing-function org-html-publish-to-html
         :auto-sitemap nil)
        ("weather-site" :components ("weather-site-org"))))

(org-publish-all t)
