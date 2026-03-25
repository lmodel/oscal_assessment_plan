package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Identifies system elements being assessed, such as components, inventory items, and locations.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AssessmentSubject  {

  private String type;
  private String description;
  private IncludeAll include-all;
  private List<SelectSubjectById> include-subjects;
  private List<SelectSubjectById> exclude-subjects;
  private String remarks;
  private List<Property> props;
  private List<Link> links;

}