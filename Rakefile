require 'jekyll'
require 'pdfkit'

namespace :jekyll do
  desc "Build the site and generate a PDF"
  task :generate_pdf do
    Jekyll::Commands::Build.process

    Dir.chdir('_site') do
      # Collect and order markdown files
      files = Dir['pages/monograph/*.md'].sort

      # Combine content of all markdown files into one
      combined_content = files.map { |file| File.read(file) }.join("\n")

      # Write combined content to a temporary HTML file
      File.write('combined.html', combined_content)

      # Generate PDF from the combined HTML file
      kit = PDFKit.new(File.new('combined.html'))
      kit.to_file('output.pdf')
    end
  end
end