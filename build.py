import pandoc4ssg

dir_struct = pandoc4ssg.DirStruct(
    root=".",
    tgt_dir_html="content/post",
    tgt_dir_tex="public/tex",
    pandoc_post_dir="pandoc_posts",
    static_tgt=None,
    public="public"
)

post_handler = pandoc4ssg.PostHandler(
    meta_keep = ["title", "subtitle", "author", "date", "categories", "tags"],
    meta_new=[("new_field", True)],
    use_toml=False,
    output_exts=".html",
    output_dir=True,
    pandoc_html_extra_args=['--citeproc'],
    dir_struct=dir_struct
)

pandoc4ssg.build(ssg_cmd="hugo -D", post_handler=post_handler)
