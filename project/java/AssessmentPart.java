package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  A partition of an assessment plan or results or a child of another part.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AssessmentPart  {

  private String uuid;
  private String name;
  private String ns;
  private String class;
  private String title;
  private String prose;
  private List<AssessmentPart> parts;
  private List<Property> props;
  private List<Link> links;

}